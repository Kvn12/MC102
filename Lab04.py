mestre = []

def numeros_soltos(x):
    '''Separa um numero em algarismos na base 10 e os coloca em uma lista, contudo em  uma ordem inversa da que era anteriormente.

    Parametros:
    x --- numero a ser separado
    '''
    soltos = []
    while x != 0:
        u = x % 10
        soltos.append(u)
        x = x // 10    
    return soltos 

def comparador_2(h):
    '''Recebe um numero, usa-o como entrada na funcao numeros_soltos e compara um item por vez da lista, recebida pela funcao, com o item correspondente da lista principal.

    Parametros:
    h --- numero a ser comparado
    '''
    s = 0
    for j in range(len(principal)):
        a = int(numeros_soltos(int(h))[j])
        if a == principal[j]:
            s += 1
    return s

                      
mestre = input().split()
k = int(mestre[1])
principal = numeros_soltos(int(mestre[0]))  


for i in range(k):
    e = input()
    t = k - i - 1
    if len(numeros_soltos(int(e))) != len(principal):       
        print("Senha incorreta")
        print("Semelhanca: Erro: quantidade de digitos incongruente")
        print("Tentativas restantes:",t)
        print()
        if t == 0:
            print("Tentativas esgotadas. Acionando defesas...")
            break     
    else:
        g = comparador_2(e)
        if g == len(principal):           
            print("Senha reconhecida. Desativando defesas...")
            break
        else:
            print("Senha incorreta")
            print("Semelhanca:",g)
            print("Tentativas restantes:",t)
            print()
            if t == 0:
                print("Tentativas esgotadas. Acionando defesas...")
                break         
                        