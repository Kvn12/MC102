from math import sqrt
import sys
sys.setrecursionlimit(1500)

def gera_tela(n, m, valor):
    '''Recebe valores para a quantidade de linhas e colunas e cria uma matriz, cujos termos sao iguais ao parametro valor.

    Parametros:
    n --- quantidade de linhas da matriz
    m --- quantidade de colunas da matriz
    valor --- caracter a ser adicionado na matriz 
    '''
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcula_distancia(i, j, i2, j2): 
    '''Recebe as coordenadas do centro de uma circunferencia e coordenada de um ponto, e com eles calcula a distancia euclidiana\
    do centro da circunferencia ate tal ponto.

    Parametros:
    i --- coordenada da linha do centro da circunferencia
    j --- coordenada da coluna do centro da circunferencia
    i2 --- coordenada da linha de um certo ponto
    j2 --- coordenada da coluna de um certo ponto
    '''
    return sqrt((j - j2) ** 2 + (i - i2) ** 2) 

def circulo_r(i, j, r, l, c, matriz):    
    '''Recebe coordenadas do centro de uma circunferencia, coordenadas de um ponto e uma matriz, e percorre-a recursivamente\ 
    alterando o item por caracter'x' nos locais em que a distancia do ponto ao centro é menor que o parametro raio. 

    Parametros:
    i --- coordenada da linha do centro da circunferencia
    j --- coordenada da coluna do centro da circunferencia
    r --- raio da circunferencia
    l --- coordenada da linha de um certo ponto
    c --- coordenada da coluna de um certo ponto
    matriz --- matriz a ser percorrida e alterada em alguns items
    '''
    dist = calcula_distancia(i, j, l, c)
    if l > len(matriz) -1:
        return
    elif c > len(matriz[0]) - 1:
        novo_c = 0
        circulo_r(i, j, r, l+1, novo_c, matriz)
    else:
        if dist <= r:
            matriz[l][c] = 'x'
        circulo_r(i, j, r, l, c+1, matriz)

def quadrado_r(i, j, a, l, c, matriz):
    '''Recebe coordenadas do centro de um quadrado, coordenadas de um ponto e uma matriz, e percorre-a recursivamente\ 
    alterando o item por caracter'x' nos locais em que a distancia do ponto ao centro é menor que a metade do parametro raio. 

    Parametros:
    i --- coordenada da linha do centro da circunferencia
    j --- coordenada da coluna do centro da circunferencia
    a --- lado do quadrado
    l --- coordenada da linha de um certo ponto
    c --- coordenada da coluna de um certo ponto
    matriz --- matriz a ser percorrida e alterada em alguns items
    '''
    if l > len(matriz)-1:
        return
    elif c > len(matriz[0])-1:
        novo_c = 0
        quadrado_r(i, j, a, l+1, novo_c, matriz)
    else:
        if abs(i-l) < a/2 and abs(j-c) < a/2:
            matriz[l][c] = 'x'
        quadrado_r(i, j, a, l, c+1, matriz)
   
def imprime(matriz):
    '''Recebe uma matriz e imprime-a item a item.

    Parametros:
    matriz --- matriz a ser impressa.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")

tamanho_tela = input().split()
q_formas = int(input())
M_linhas = int(tamanho_tela[0]) 
N_colunas = int(tamanho_tela[1]) 
tela = gera_tela(M_linhas, N_colunas, '-')

for a in range(q_formas):
    descricao = input().split()
    i = int(descricao[1])
    j = int(descricao[2])
    l_r = int(descricao[3])
    if descricao[0] == 'circulo':  
        circulo_r(i, j, l_r, 0, 0, tela)
    elif descricao[0] == 'quadrado': 
        quadrado_r(i, j, l_r, 0, 0, tela)

imprime(tela)