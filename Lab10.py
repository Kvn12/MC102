dossie = {}
evidencias = set()
numero_de_suspeitos = 0
nomes_suspeitos = []
while True:
    entrada = input().split(':')   #nome
    nome = entrada[1].strip() 
    caracteristicas = set()
    while True:
        infos = input().split(':')
        if infos[0] != '-' and infos[0] != '--': 
            infos_ok = infos[1].strip() 
            caracteristicas.add(infos_ok)
        else:
            break
    dossie[nome] = caracteristicas
    if infos[0] == '--':
        entrada_evidencias = input().split(':')
        entrada_evidencias = entrada_evidencias[1].strip()
        evidencias.add(entrada_evidencias)
        while True:
            evidencia = input().split(':')
            if evidencia[0] != '---':
                caracteristica_evidencia = evidencia[1].strip()
                evidencias.add(caracteristica_evidencia)
            else: 
                break 
        if evidencia[0] == '---': 
            break

for chave, valor in dossie.items():
    semelhancas = valor.intersection(evidencias)
    if len(semelhancas) == len(evidencias):
        numero_de_suspeitos += 1
        nomes_suspeitos.append(chave) 
if numero_de_suspeitos == 1:
    print('Suspeito(a):')
    print(nomes_suspeitos[0])
elif numero_de_suspeitos == 0:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
else:
    em_ordem = sorted(nomes_suspeitos)
    print('Suspeitos(as):') 
    for suspeito in em_ordem:
        print(suspeito)