def codificar(string, linha):
    '''Recebe uma string, verifica se e pertencente a uma linha impar ou par e a codifica conforme sua origem.

    Parametros:
    string --- string a ser codificada
    linha --- numero da linha da string
    '''
    lista_ASCII = []   
    if (linha + 1) % 2 != 0:  #IMPAR
        lista_hex = []
        lista_hex_enxertada = []
        lista_hex_enxertada_upper = []
        for car in string:
            caracter_ASCII = str(ord(car))
            lista_ASCII.append(caracter_ASCII) 
        for i in lista_ASCII:                  
            caracter_hex = hex(int(i))
            lista_hex.append(caracter_hex[2:]) 
        for i in lista_hex:
            lista_hex_enxertada.append(i.zfill(Enxerto)) 
        for i in lista_hex_enxertada:
            lista_hex_enxertada_upper.append(i.upper())

        print("".join(lista_hex_enxertada_upper))
    else:                 #PAR
        string_invertida = string[::-1]
        lista_oct = []
        lista_oct_enxertada = []
        lista_oct_enxertada_upper = []
        for car in string_invertida:
            caracter_ASCII = str(ord(car))
            lista_ASCII.append(caracter_ASCII)
        for i in lista_ASCII:
            caracter_oct = oct(int(i))    
            lista_oct.append(caracter_oct[2:])
        for i in lista_oct:
            lista_oct_enxertada.append(i.zfill(Enxerto))
        for i in lista_oct_enxertada:
            lista_oct_enxertada_upper.append(i.upper())      

        print("".join(lista_oct_enxertada_upper))

def decodificar(string, linha):
    '''Recebe uma string, verifica se e pertencente a uma linha impar ou par e a decodifica conforme sua origem.

    Parametros:
    string --- string a ser codificada
    linha --- numero da linha da string
    '''
    lista_ASCII_Decod = []
    if (linha + 1) % 2 != 0:  #IMPAR  
        lista_chr = [] 
        for i in range(0, len(string), Enxerto):
            str_B10 = int(string[i:i+Enxerto], 16)
            lista_ASCII_Decod.append(str_B10)
        for i in lista_ASCII_Decod:
            lista_chr.append(chr(i))
        print("".join(lista_chr))
    else:                   #PAR
        lista_chr_oct = []
        for i in range(0, len(string), Enxerto):
            str_B8 = int(string[i:i+Enxerto], 8)
            lista_ASCII_Decod.append(str_B8)
        for i in lista_ASCII_Decod:
            lista_chr_oct.append(chr(i))
        lista_chr_oct.reverse()
        print("".join(lista_chr_oct))

n = [int(x) for x in input().split()]  #Modo, Enxerto, Linhas
Modo = n[0]
Enxerto = n[1]
quantidade_linhas = n[2]
for linha in range(quantidade_linhas):
    string = input()
    if Modo == 1:  #CODIFICAR 
        codificar(string, linha)
    elif Modo == 2: #DECODIFICAR
        decodificar(string, linha)