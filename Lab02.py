nome = input()
n = int(input( ))

data_formatada = []
visu = []

x = n
y = 0
z = 0
w = 0
soma_18 = 0
soma_19 = 0
soma_20 = 0

for i in range(n):
    data_formatada.append(input().split('-')[0])
    visu.append(input())
for k in range(n):
    if data_formatada[k] == '2018':
         soma_18 = soma_18 + int(visu[k])
         y += 1 
    elif data_formatada[k] == '2019':
         soma_19 = soma_19 + int(visu[k])
         z += 1 
    elif data_formatada[k] == '2020':
         soma_20 = soma_20 + int(visu[k]) 
         w += 1  
    else:
        x -= 1
         
soma_total = soma_18 + soma_19 + soma_20

print("Canal:", nome)
print("Total de views do trienio:", soma_total)
media_18 = soma_18 / y
media_19 = soma_19 / z
media_20 = soma_20 / w

if soma_total != 0 and x != 0:

    mediaTotal = (soma_total / x)
    porc_18 = soma_18 / soma_total * 100
    porc_19 = soma_19 / soma_total * 100
    porc_20 = soma_20 / soma_total * 100

    print("Media de views do trienio:",format(mediaTotal,'.2f'))
    print()
    print("2018")
    print("Total:", soma_18)
    print("Porcentagem das views do trienio:", format(porc_18,'.2f'))
    print("Media:", format(media_18,'.2f'))

    print()
    print("2019")
    print("Total:", soma_19)
    print("Porcentagem das views do trienio:",format(porc_19, '.2f'))
    print("Media:",format(media_19,'.2f')) 

    print()
    print("2020")
    print("Total:", soma_20)
    print("Porcentagem das views do trienio:",format(porc_20, '.2f'))
    print("Media:", format(media_20,'.2f'))

elif x == 0:

    mediaTotal = 0
    porc_18 = soma_18 / soma_total * 100
    porc_19 = soma_19 / soma_total * 100
    porc_20 = soma_20 / soma_total * 100

    print("Media de views do trienio:",format(mediaTotal,'.2f'))
    print()
    print("2018")
    print("Total:", soma_18)
    print("Porcentagem das views do trienio:", format(porc_18,'.2f'))
    print("Media:", format(media_18,'.2f'))

    print()
    print("2019")
    print("Total:", soma_19)
    print("Porcentagem das views do trienio:",format(porc_19, '.2f'))
    print("Media:",format(media_19,'.2f')) 

    print()
    print("2020")
    print("Total:", soma_20)
    print("Porcentagem das views do trienio:",format(porc_20, '.2f'))
    print("Media:", format(media_20,'.2f'))


elif soma_total == 0: 
    mediaTotal = (soma_total / x)  
    print("Media de views do trienio:",format(mediaTotal,'.2f'))
    print()
    print("2018")
    print("Total:", soma_total)
    print("Porcentagem das views do trienio: indeterminada")
    print("Media: 0.00")

    print()
    print("2019")
    print("Total:", soma_total)
    print("Porcentagem das views do trienio: indeterminada")
    print("Media: 0.00") 

    print()
    print("2020")
    print("Total:", soma_total)
    print("Porcentagem das views do trienio: indeterminada")
    print("Media: 0.00")
