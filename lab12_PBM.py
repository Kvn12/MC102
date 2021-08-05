from math import sqrt

def cria_matriz(n, m, valor=1):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcula_distancias(i, j, i2, j2): 
    return sqrt((j - j2) ** 2 + (i - i2) ** 2) 

def circulo_r(i, j, r, l, c, matriz):    
    if l > len(matriz)-1 and c > len(matriz[0])-1:
        return matriz

    elif l > len(matriz)-1 or c > len(matriz[0])-1:
        if c > len(matriz[0])-1:
            c_novo =  0
            circulo_r(i, j, r, l + 1, c_novo, matriz)
        elif l > len(matriz)-1:
            return matriz

    else:
        dist = calcula_distancias(i, j, l, c)
        if dist <= r:
            matriz[l][c] = 0
        circulo_r(i, j, r, l, c+1, matriz)
        return matriz

def quadrado_r(i, j, a, l, c, matriz):
    if l > len(matriz)-1 and c > len(matriz[0])-1:
        return matriz

    elif l > len(matriz)-1 or c > len(matriz[0])-1:
        if c > len(matriz[0])-1:
            c_novo =  0
            quadrado_r(i, j, a, l + 1, c_novo, matriz)
        elif l > len(matriz)-1:
            return matriz

    else:
        if abs(i-l) <= a/2 and abs(j-c) <= a/2:
            matriz[l][c] = 0
        quadrado_r(i, j, a, l, c+1, matriz)
        return matriz

   
def imprime(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j == len(m[i]) - 1:
                print(m[i][j])
            else:
                print(m[i][j], end=" ")

def salva(arquivo, matriz):
    with open(arquivo, 'w') as f:
        f.write('P1\n')
        f.write(f'{len(matriz[0])} {len(matriz)}\n')
        for linha in matriz:
            f.write(' '.join(map(str, linha)))
            f.write('\n')


tamanho_tela = input().split()
q_formas = int(input())
M_linhas = int(tamanho_tela[0]) 
N_colunas = int(tamanho_tela[1]) 
tela = cria_matriz(M_linhas, N_colunas)

for a in range(q_formas):
    descricao = input().split()
    i = int(descricao[1])
    j = int(descricao[2])
    l_r = int(descricao[3])
    if descricao[0] == 'circulo':  #circulo i j r
        tela = circulo_r(i, j, l_r, 0, 0, tela)
    elif descricao[0] == 'quadrado':  #quadrado i j l
        tela = quadrado_r(i, j, l_r, 0, 0, tela)


salva('teste1.pbm', tela)
