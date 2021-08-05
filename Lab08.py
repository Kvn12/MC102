def variavel(expressao):
    '''Recebe uma lista cujos itens sao termos de uma expressao e verifica se e uma expressao de atribuicao de variavel.

    Parametros:
    expressao --- lista a ser avaliada 
    '''
    if not expressao[0].isdigit() and expressao[1] == '=':  
        return True
    else:
        return False

def troca_variaveis(expressao):
    '''Recebe uma lista, verifica se existem termos que referenciem a variaveis, e troca esses termos pelos seus valores\
    se existirem, e se nao, retorna None e imprime uma mensagem de erro.

    Parametros:
    expressao --- lista a ter variaveis trocadas
    '''
    expressao_sem_variaveis = []
    for a in expressao:
        if not a.isdigit() and a != '<' and a != '>' and a != '==' and a != '!=' and a != 'AND' and a != 'OR' and a != '<=' and a != '>=' and a != '+' and a != '-':
            conferindo_existencia = variaveis.get(a,None)
            if conferindo_existencia == None:
                print(f'Erro de referencia: a variavel {a} nao foi definida.')
                return None
            else:
                expressao_sem_variaveis.append(variaveis.get(a)[0])
        else:
            expressao_sem_variaveis.append(a)
    return expressao_sem_variaveis

def soma_sub(expressao):
    '''Recebe uma lista e realiza as operacoes de soma e subtracao se existirem, sempre da esquerda para a direita.

    Parametros:
    expressao --- lista a ter os valores somados
    '''
    while '+'in expressao or '-' in expressao:
        for i in range(len(expressao)):  
            if expressao[i] == '+':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i)) 
                expressao.pop(i-1)
                resultado = x + y
                expressao.insert(i-1, resultado)
                break
            elif expressao[i] == '-':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i)) 
                expressao.pop(i-1)
                resultado = x - y
                expressao.insert(i-1, resultado)
                break
    return expressao

def comparacao_1(expressao):
    '''Recebe uma lista e realiza as operacoes de comparacao, de acordo com a ordem em que aparecem, sempre da esquerda\
    para a direita.

    Parametros:
    expressao --- lista a ser realizada as operacoes
    '''
    while '>'in expressao or '<' in expressao or '>=' in expressao or '<=' in expressao or '!=' in expressao or '==' in expressao:
        for i in range(len(expressao)):   
            if expressao[i] == '>':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i))
                expressao.pop(i-1) 
                valor = x > y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
            if expressao[i] == '<':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i)) 
                expressao.pop(i-1)
                valor = x < y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
            if expressao[i] == '>=':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i))
                expressao.pop(i-1) 
                valor = x >= y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
            if expressao[i] == '<=':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i))
                expressao.pop(i-1) 
                valor = x <= y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
            if expressao[i] == '==':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i))
                expressao.pop(i-1) 
                valor = x == y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
            if expressao[i] == '!=':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i))
                expressao.pop(i-1) 
                valor = x != y
                if valor == True:
                    valor = 1
                else:
                    valor = 0
                expressao.insert(i-1, valor)
                break
    return expressao

def comparacao_2(expressao):
    '''Recebe uma lista e realizada as operacoes de comparacao composta, da esquerda para a direita.

    Parametros:
    expressao --- lista a ser realizada as operacoes
    '''
    while 'OR' in expressao or 'AND' in expressao:
        for i in range(len(expressao)):  
            if expressao[i] == 'AND':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i)) 
                expressao.pop(i-1)
                resultado = x and y
                expressao.insert(i-1, resultado)
                break                    
            if expressao[i] == 'OR':
                x = int(expressao.pop(i-1))
                y = int(expressao.pop(i)) 
                expressao.pop(i-1)
                resultado = x or y
                expressao.insert(i-1, resultado)
                break
    return expressao

variaveis = {}
while True:
    try: 
        entrada = input().split()
        if len(entrada) != 1:
            if entrada[1] == '=' and (not entrada[0].isalnum() or entrada[0][0].isdigit() ): 
                print(f'Erro de sintaxe: {entrada[0]} nao e um nome permitido para uma variavel.') 
            else:
                verificacao = variavel(entrada)
                if verificacao == True:
                    verificacao_2 = troca_variaveis(entrada[2:])
                    if verificacao_2 != None:
                        variaveis[entrada[0]] = comparacao_2(comparacao_1(soma_sub(troca_variaveis(entrada[2:]))))
                else:
                    verificacao_2 = troca_variaveis(entrada)
                    if verificacao_2 != None:                                                                                 
                        resultado = comparacao_2(comparacao_1(soma_sub(verificacao_2)))
                        print(resultado[0])
        else:
            verificacao = variaveis.get(entrada[0],None)
            if verificacao == None and not entrada[0].isnumeric():
                print(f'Erro de referencia: a variavel {entrada[0]} nao foi definida.')
            else:
                if entrada[0].isdigit():
                    print(entrada[0])
                else:
                    print(verificacao[0])
                
    except EOFError:
        break
print("Encerrando... Bye-bye.")

