from math import log2

def divisao(dicio, base, altura, i):
    '''Calcula quantas vezes uma potencia de dois cabe em determinado espaço, delimitado pela base e altura, e calcula recursivamente\
    para outras potencias de dois menores que a inicial, de modo a cobrir todo o espaço com quadrados de largura iguais a potencias de\
    dois e armazena os resultados em um dicionario.

    Parametros:
    dicio --- dicionario que armazena os resultados das divisoes
    base --- dimensao da base do espaço em questao
    altura --- dimensao da altura do espaço em questao
    i --- valor do expoente a ser utilizado, sempre comeca com o maior valor possivel
    '''
    if i < 0 or base == 0 or altura == 0:
        return 
    divisao_base = base // 2**i
    divisao_altura = altura // 2**i

    if i not in dicio:
        dicio[i] = divisao_base*divisao_altura
    else:
        dicio[i] += divisao_base*divisao_altura

    divisao(dicio, base, altura-(2**i)*divisao_altura, i-1)
    divisao(dicio, base-(2**i)*divisao_base, 2**i*divisao_altura, i-1)

def soma_submagias(submagias):
    '''Calcula a soma de todos os valores de um dicionario, referentes a quantidade de submagias utilizadas no total.

    Parametros:
    submagias --- dicionario a ter seus valores calculados
    '''
    soma = 0
    for valores in submagias.values():
        soma += valores
    return soma

def calculo_pm(submagias):
    '''Calcula a soma do produto de cada valor do dicionario com a potencia de dois cujo expoente e a sua chave.

    Parametros:
    submagias --- dicionario a ter esse valor calculado
    '''
    soma = 0
    for key in submagias:
        soma +=  submagias[key] * (2**key)
    return soma

dimensoes = input().split()
base = int(dimensoes[0])
altura = int(dimensoes[1])
submagias = dict()

if base < altura:
    i = int(log2(base))
    divisao(submagias, base, altura, i)
else:
    i = int(log2(altura))
    divisao(submagias, base, altura, i)

total_submagias = soma_submagias(submagias)
total_pm = calculo_pm(submagias)

#Impressao
print('---')
print("Grimorio de Teraf L'are")
print('---')

for key in sorted(submagias.keys()):
    if submagias[key] != 0:
        print(f'{submagias[key]} submagia(s) de nivel {key}')

print('---')
print(f'Total de submagia(s) conjurada(s): {total_submagias}')
print(f'Total de PM gasto: {total_pm}')
print('---')