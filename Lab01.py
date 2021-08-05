nome_material = input()
ponto_fusao = float(input())
ponto_ebulicao = float(input())
temp_atual = float(input())

print("Material:", nome_material)
print("Ponto de fusao (Celsius):", format(ponto_fusao, '.2f'))
print("Ponto de ebulicao (Celsius):", format(ponto_ebulicao, '.2f'))

c = 5* (temp_atual - 32) / 9 

temp_celsius = round(c, 2)
print("Temperatura atual (Celsius):", format(temp_celsius, '.2f'))

if temp_celsius >= ponto_ebulicao:
    print("Estado fisico do material: Gasoso")
elif temp_celsius >= ponto_fusao:
    print("Estado fisico do material: Liquido")
else: 
    print("Estado fisico do material: Solido")

