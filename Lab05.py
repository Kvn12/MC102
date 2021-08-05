def segunda(x):
    '''Avalia cada caracter de uma string e retorna um valor referente a quantidade de caracteres minusculos.

    Parametros:
    x --- string a ser avaliada
    '''
    q = 0
    for car in x: 
        if car.islower():
            q += 1
    return q

def terca(y):
    '''Avalia cada caracter de uma string e retorna um valor referente a quantidade de caracteres maiusculos.

    Parametros:
    y --- string a ser avaliada
    '''
    q = 0
    for car in y:
        if car.isupper():
            q += 1
    return q

def quarta(z):
    '''Avalia cada caracter de uma string e retorna um valor referente a quantidade de caracteres do alfabeto.

    Parametros:
    z --- string a ser avaliada
    '''
    q = 0
    for car in z:
        if car.isalpha():
            q += 1
    return q

def quinta(w):
    '''Recebe uma string e retorna um valor referente a quantidade de caracteres.

    Parametros:
    w --- string a calcular a quantidade de caracteres
    '''
    k = w.split()
    return len(k) 

def sexta(u):
    '''Soma os valores ASCII de cada caracter em uma string.

    Parametros:
    u --- string a ser analisada
    '''
    q = 0
    for car in u:
        q += ord(car)
    return q           
  

dia = []
dia = input().split()
dia_semana = dia[0]
entradas = int(dia[1])
t = []

for i in range(entradas):
    t.append(input())
if dia_semana == "Segunda": #ordenar os endereços de forma crescente com base no número de letras minúsculas da string
    ordenado = sorted(t, key=segunda)
    for c in range(len(ordenado)):
        print(ordenado[c])
        
if dia_semana == "Terca": #ordenar os endereços de forma decrescente com base no número de letras maiúsculas da string
    ordenado = sorted(t, key=terca ,reverse=True)
    for v in range(len(ordenado)):
        print(ordenado[v])

if dia_semana == "Quarta": #ordenar os endereços de forma crescente com base no número de caracteres da string que são letras do alfabeto.
    ordenado = sorted(t, key=quarta)
    for b in range(len(ordenado)):
        print(ordenado[b])
  
if dia_semana == "Quinta": #ordenar os endereços de forma crescente com base no número de palavras
    ordenado = sorted(t, key=quinta)
    for n in range(len(ordenado)):
        print(ordenado[n])

if dia_semana == "Sexta": #ordenar os endereços de forma decrescente com base na soma dos valores ASCII dos caracteres da string (incluindo os caracteres que são espaços em branco 
    ordenado = sorted(t, key=sexta, reverse=True)
    for m in range(len(ordenado)):
        print(ordenado[m]) 