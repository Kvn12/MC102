class Medalutador:
    '''Classe que contem os atributos de cada medalutador,incluindo seu numero ID no campeonato e uma classe com seu medabot e suas medapecas.

    '''
    def __init__(self, ID, Medabot):
        self.ID = ID
        self.Medabot = Medabot

    def obter_ID(self):
        return self.ID

    def __repr__(self):
        return str(self.ID)
        
    def medapeca_nova(self):
        return self.Medabot.Medapecas.medapeca_nova

class Medabot:
    '''Classe que contem os atributos de cada medabot.

    '''
    def __init__(self,habilidade_inicial, habilidade_atual ,recuperacao, bonus_de_ataque, bonus_de_defesa,\
         pontos_do_torso, pontos_do_braco_d, pontos_do_braco_e, pontos_das_pernas, medapeca_nova ):
        self.habilidade_inicial = habilidade_inicial
        self.habilidade_atual = habilidade_atual
        self.recuperacao = recuperacao
        self.bonus_de_ataque = bonus_de_ataque
        self.bonus_de_defesa = bonus_de_defesa
        self.pontos_do_torso = pontos_do_torso  
        self.pontos_do_braco_d = pontos_do_braco_d
        self.pontos_do_braco_e = pontos_do_braco_e
        self.pontos_das_pernas = pontos_das_pernas
        self.medapeca_nova = medapeca_nova 
        
    def ataque(self): 
        return max(self.pontos_do_braco_d) + max(self.pontos_do_braco_e) + self.bonus_de_ataque 

    def defesa(self):
        return max(self.pontos_do_torso) + max(self.pontos_das_pernas) + self.bonus_de_defesa    
       
def simular_torneios_de_cyberlutas(lista_de_medalutadores):
    '''Simula o torneio de cyberlutas.

    Parametros:
    lista_de_medalutadores --- lista com os medalutadores que participarao do torneio
    '''
    lista_torneio_principal = []
    lista_de_repescagem     = []
    for medalutador in lista_de_medalutadores:
        lista_torneio_principal.append(medalutador)
    while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
        lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
        lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
    i = lista_torneio_principal.pop(0)
    j = lista_de_repescagem.pop(0)
    print('Cyberluta Final')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem): 
    '''Simula cada rodada do torneio.

    Parametros:
    lista_de_medalutadores --- lista com os medalutadores no torneio principal
    lista_de_repescagem --- lista com os medalutadores para o torneio de repescagem
    '''
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores
    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0) 
        j = lista_de_medalutadores.pop(0)
        if i.obter_ID() > j.obter_ID():
            i, j = j, i                    
        if lista_de_repescagem != None:
            print('Cyberluta do Torneio Principal')
        else:
            print('Cyberluta da Repescagem')
        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)
        k = batalhar(i, j)
        imprimir_resultado_da_batalha(k)
        if lista_de_repescagem != None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)
        lista_de_vencedores.append(k)
    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores

def batalhar(i, j):
    '''Recebe dois Medalutadores e compara seus pontos de defesa e ataque, habilidade e seus IDs, e atraves de um procedimento devolve o campeao.
    Chama duas outras funcoes com esses medalutadores para troca de pecas e decrescimo de habilidades.

    Parametros:
    i --- Campeao a batalhar
    j -- Campeao a batalhar
    '''
    if (i.Medabot.ataque() > j.Medabot.defesa() or j.Medabot.ataque() > i.Medabot.defesa()) and i.Medabot.ataque()-j.Medabot.defesa() != j.Medabot.ataque() - i.Medabot.defesa():                                                
        if i.Medabot.ataque()-j.Medabot.defesa() > j.Medabot.ataque()-i.Medabot.defesa():                                                                                         
            vencedor = i
            perdedor = j
        else: 
            vencedor = j    
            perdedor = i
    elif i.Medabot.habilidade_atual != j.Medabot.habilidade_atual:                               
        if i.Medabot.habilidade_atual > j.Medabot.habilidade_atual:                              
            vencedor = i
            perdedor = j
        else:
            vencedor = j
            perdedor = i              
    else:
        if i.ID < j.ID:                                                
            vencedor = i                                                
            perdedor = j
    troca_medapecas(vencedor, perdedor)
    perda_habilidade(vencedor, perdedor)
                                                           
    return vencedor
 
def troca_medapecas(vencedor, perdedor):
    '''Recebe dois medalutadores apos uma batalha, analisa a peca que sera mais valiosa e tira do perdedor e entrega ao vencedor.

    Parametros:
    vencedor --- medalutador que ganhou a batalha
    perdedor --- medalutador que perdeu a batalha
    '''
    Direito = max(perdedor.Medabot.pontos_do_braco_d) - max(vencedor.Medabot.pontos_do_braco_d)
    Esquerdo =  max(perdedor.Medabot.pontos_do_braco_e) - max(vencedor.Medabot.pontos_do_braco_e) 
    Pernas = max(perdedor.Medabot.pontos_das_pernas) - max(vencedor.Medabot.pontos_das_pernas)
    Torso = max(perdedor.Medabot.pontos_do_torso) - max(vencedor.Medabot.pontos_do_torso)
    medapecas = []
    medapecas.append(Torso)           
    medapecas.append(Esquerdo)
    medapecas.append(Direito)
    medapecas.append(Pernas)
    posicao_peca_mais_valiosa = medapecas.index(max(medapecas))  #posicao da peca a ser trocada
    u = medapecas[posicao_peca_mais_valiosa]
    if u == Torso:
        vencedor.Medabot.pontos_do_torso.append(max(perdedor.Medabot.pontos_do_torso))     
        vencedor.Medabot.medapeca_nova.append("T")
        vencedor.Medabot.medapeca_nova.append(max(perdedor.Medabot.pontos_do_torso))
        perdedor.Medabot.pontos_do_torso.remove(max(perdedor.Medabot.pontos_do_torso))         
    elif u == Esquerdo:
        vencedor.Medabot.pontos_do_braco_e.append(max(perdedor.Medabot.pontos_do_braco_e))
        vencedor.Medabot.medapeca_nova.append("E")
        vencedor.Medabot.medapeca_nova.append(max(perdedor.Medabot.pontos_do_braco_e))
        perdedor.Medabot.pontos_do_braco_e.remove(max(perdedor.Medabot.pontos_do_braco_e))
    elif u == Direito:
        vencedor.Medabot.pontos_do_braco_d.append(max(perdedor.Medabot.pontos_do_braco_d))
        vencedor.Medabot.medapeca_nova.append("D")
        vencedor.Medabot.medapeca_nova.append(max(perdedor.Medabot.pontos_do_braco_d))
        perdedor.Medabot.pontos_do_braco_d.remove(max(perdedor.Medabot.pontos_do_braco_d))
    else:
        vencedor.Medabot.pontos_das_pernas.append(max(perdedor.Medabot.pontos_das_pernas))
        vencedor.Medabot.medapeca_nova.append("P")
        vencedor.Medabot.medapeca_nova.append(max(perdedor.Medabot.pontos_das_pernas))
        perdedor.Medabot.pontos_das_pernas.remove(max(perdedor.Medabot.pontos_das_pernas))
   
def perda_habilidade(vencedor, perdedor):
    '''Realiza o decrescimo na habilidade dos medalutadores apos uma batalha,
    sendo que esse decrescimo ocorre de maneira diferente para o vencedor e para o perdedor.
    Alem de considerar a recuperacao de cada medalutador para a proxima batalha.

    Parametros:
    vencedor --- medalutador que ganhou a batalha, habilidade decrementada em relacao ao perdedor
    perdedor --- medalutador que perdeu a batalha, habilidade decrementada pela metade.
    '''   
    desgaste_vencedor = vencedor.Medabot.habilidade_atual - perdedor.Medabot.habilidade_atual
    desgaste_perdedor = perdedor.Medabot.habilidade_atual // 2
    h_vencedor = desgaste_vencedor + vencedor.Medabot.recuperacao
    h_perdedor = desgaste_perdedor + perdedor.Medabot.recuperacao
    if desgaste_vencedor < 0:
        h_vencedor = vencedor.Medabot.recuperacao
        if h_vencedor <= vencedor.Medabot.habilidade_inicial:  
            vencedor.Medabot.habilidade_atual = h_vencedor
        else:
            vencedor.Medabot.habilidade_atual = vencedor.Medabot.habilidade_inicial
    else:
        if h_vencedor <= vencedor.Medabot.habilidade_inicial:  
            vencedor.Medabot.habilidade_atual = h_vencedor
        else:
            vencedor.Medabot.habilidade_atual = vencedor.Medabot.habilidade_inicial     
    if desgaste_perdedor < 0:
        h_perdedor = perdedor.Medabot.recuperacao
        if h_perdedor <= perdedor.Medabot.habilidade_inicial:
            perdedor.Medabot.habilidade_atual = h_perdedor
        else:
            perdedor.Medabot.habilidade_atual = perdedor.Medabot.habilidade_inicial
    else:
        if h_perdedor <= perdedor.Medabot.habilidade_inicial:
            perdedor.Medabot.habilidade_atual = h_perdedor
        else:
            perdedor.Medabot.habilidade_atual = perdedor.Medabot.habilidade_inicial

def imprimir_ficha_tecnica(i, j):
    '''Imprime a ficha tecnica de cada medalutador.

    Parametros:
    i --- medalutador
    j --- medalutador
    ''' 
    lista_ficha = []
    lista_ficha.append(i)                
    lista_ficha.append(j)
    for k in lista_ficha:
        print(f'\tA{k.ID} = E{max(k.Medabot.pontos_do_braco_e)} + D{max(k.Medabot.pontos_do_braco_d)} + {k.Medabot.bonus_de_ataque} = {max(k.Medabot.pontos_do_braco_d) + max(k.Medabot.pontos_do_braco_e) + k.Medabot.bonus_de_ataque}') 
        print(f'\tD{k.ID} = T{max(k.Medabot.pontos_do_torso)} + P{max(k.Medabot.pontos_das_pernas)} + {k.Medabot.bonus_de_defesa} = {max(k.Medabot.pontos_do_torso) + max(k.Medabot.pontos_das_pernas) + k.Medabot.bonus_de_defesa}')
        print(f'\tH{k.ID} = {k.Medabot.habilidade_atual}')    

def imprimir_resultado_da_batalha(k):
    '''Imprime o resultado apos cada batalha, informando quem ganhou e qual peca ganhou de seu oponente.

    Parametros:
    k --- medalutador campeao da batalha
    '''
    z = k.Medabot.medapeca_nova[len(k.Medabot.medapeca_nova) - 1]       
    w = k.Medabot.medapeca_nova[len(k.Medabot.medapeca_nova) - 2]
    print(f'Medalutador {k} venceu e recebeu a {w}{z}\n')
 
lista_de_medalutadores = []
N = int(input()) #quantidade de medalutadores
for e in range(N):
    id = e + 1
    partes = []
    partes_novas = []
    T = []
    D = []
    E = []
    P = []
    primeira_linha = [int(x) for x in input().split()]    #entrarao 3 dados: Habilidade, Recuperacao, Quantidade de medapecas  
    segunda_linha = [int(x) for x in input().split()]    #bonus: ataque e defesa 

    for a in range(primeira_linha[2]):
        partes.append(input()) #medapecas, T E D P 
    for b in partes:
        if b[0] == 'T':         #torso
            T.append(int(b[2:]))
        elif b[0] == 'D':       #braço direito
            D.append(int(b[2:]))
        elif b[0] == 'E':       #braço esquerdo
            E.append(int(b[2:]))
        elif b[0] == 'P':       #pernas
            P.append(int(b[2:]))
    
    M = Medabot(habilidade_inicial=primeira_linha[0], habilidade_atual=primeira_linha[0] ,recuperacao=primeira_linha[1],\
         bonus_de_ataque=segunda_linha[0], bonus_de_defesa=segunda_linha[1], pontos_do_torso=T, pontos_do_braco_d=D, pontos_do_braco_e=E, pontos_das_pernas=P, medapeca_nova=partes_novas)
    x = Medalutador(ID = id, Medabot=M)
    lista_de_medalutadores.append(x)

simular_torneios_de_cyberlutas(lista_de_medalutadores)
  
