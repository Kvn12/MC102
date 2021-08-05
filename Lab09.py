def intersecao(m, n):
    '''Recebe duas matrizes cujas linhas sao conjuntos e compara cada linha em busca de intersecoes, as quais se existirem\
    sao colocadas como linhas de uma nova matriz, a qual e retornada.

    Parametros:
    m --- matriz a ser comparada
    n --- matriz a ser comparada  
    '''
    matriz_intersecao = []
    for i in range(len(m)):
        for j in range(len(n)):
            intersecao = m[i].intersection(n[j])
            if len(intersecao) != 0:
                matriz_intersecao.append(intersecao)
    return matriz_intersecao 

while True:  
    linha_1 = input().split()
    if linha_1[0] != '0':
        m = []
        n = []
        for i in range(int(linha_1[0])):                    
            linha = input().split()
            s = set()
            m.append(s)
            for j in range(len(linha)):
                m[i].add(int(linha[j])) 
        for i in range(int(linha_1[1])):
            linha = input().split()
            s = set()
            n.append(s)
            for j in range(len(linha)):
                n[i].add(int(linha[j]))    
        matriz_intersecao = intersecao(m, n)
        print(len(m)+len(n)-len(matriz_intersecao), "x", len(m)+len(n)-len(matriz_intersecao[0]))
    else:
        break



