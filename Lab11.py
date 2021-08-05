from math import sqrt 

def calcula_distancias(coordenadas, y):
    '''Recebe uma lista com valores de coordenadas(x,y) e um valor para y, e para cada coordenada calcula a disrtancia\
    em relaçao ao  ponto (0, y). Retorna uma lista com todas as distancias.

    Parametros:
    coordenadas --- lista com coordenadas de pontos no plano cartesiano.
    y --- coordenada do ponto a ser calculado as distancias com os pontos.
    ''' 
    distancias = []
    for i in coordenadas:
        distancia = sqrt((i[0]) ** 2 + (i[1] - y) ** 2) 
        distancias.append(distancia)
    return distancias

def Acha_maior_distancia(lista):  
    '''Recebe uma lista com valores de distancias, coloca em ordem crescente e devolve o maior valor dessa lista.

    Parametros:
    lista --- lista a ser ordenada
    '''
    for i in range(len(lista) - 1):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        lista[min], lista[i] = lista[i], lista[min]
    return lista[len(lista) - 1] #retorna a maior distancia

def buscaBinaria(Y_muralha, coordenadas): 
    '''Recebe um valor para y e uma lista como coordenadas de pontos no plano. Faz uma busca binaria comparando\
    as distancias (calculadas atraves de outra funcao) dos valores das coordenadas em relacao a y, de modo a encontrar\
    a menor distancia, uma vez que os valores das distancias sao crescentes tanto para cima quanto para baixo do valor\
    de y', que é o retorno da funcao.

    Parametros:
    Y_muralha --- valor de um dos extremos do espaço da busca binária
    coordenadas --- lista com as coordenadas de pontos a serem comparadas as distancias  
    '''
    e = 0
    d = Y_muralha - 1    
    while e <= d:
        m = (e+d) // 2
        dist_M = Acha_maior_distancia(calcula_distancias(coordenadas, m))
        dist_M_up = Acha_maior_distancia(calcula_distancias(coordenadas, m+1))
        dist_M_down = Acha_maior_distancia(calcula_distancias(coordenadas, m-1))
        if dist_M < dist_M_up and dist_M < dist_M_down:
            return m
        elif dist_M > dist_M_up:
            e = m + 1
        elif dist_M > dist_M_down:
            d = m - 1

while True:
    primeira_linha = input().split()
    N = int(primeira_linha[0])
    Y_muralha = int(primeira_linha[1])
    coordenadas = []
    if N != 0 and Y_muralha !=0:
        for i in range(N):
            x_y = [int(x) for x in input().split()]
            coordenadas.append(x_y)
        print(buscaBinaria(Y_muralha, coordenadas))
    else: 
        break