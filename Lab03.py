while True:
    dimensao_tabuleiro = int(input()) 
    if dimensao_tabuleiro != 0:
        info_peça = input().split()
        nome_peça = info_peça[0]
        coluna_peça = ord(info_peça[1]) - 96
        linha_peça = int(info_peça[2])
        if nome_peça == 'Torre':
            print(f'Movimentos para a peca Torre a partir da casa {info_peça[1]}{linha_peça}.') 
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if j == 0:
                        print(i, end=' ')
                    elif j == coluna_peça:
                        if i == linha_peça:
                            print('o', end=' ')
                        else:
                            print('x', end=' ')
                    elif i == linha_peça:
                        print('x', end=' ')
                    else:
                        print('-', end=' ')
                print()

        elif nome_peça == 'Bispo':
            print(f'Movimentos para a peca Bispo a partir da casa {info_peça[1]}{linha_peça}.') 
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if j == 0:
                        print(i, end=' ')
                    elif j == coluna_peça:
                        if i == linha_peça:
                            print('o', end=' ')
                        else:
                            print('-', end=' ')
                    elif abs(j - coluna_peça )== abs(i - linha_peça):
                        print('x', end=' ')
                    else:
                        print('-', end=' ')
                print()

        elif nome_peça == 'Dama':
            print(f'Movimentos para a peca Dama a partir da casa {info_peça[1]}{linha_peça}.') 
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if j == 0:
                        print(i, end=' ')
                    elif j == coluna_peça:
                        if i == linha_peça:
                            print('o', end=' ')
                        elif i != linha_peça:
                            print('x', end=' ')
                        else:
                            print('-', end=' ')
                    elif abs(j - coluna_peça )== abs(i - linha_peça):
                        print('x', end=' ')
                    elif i == linha_peça:
                        print('x', end=' ')
                    else:
                        print('-', end=' ')
                print()   

        elif nome_peça == 'Rei':
            print(f'Movimentos para a peca Rei a partir da casa {info_peça[1]}{linha_peça}.')  
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if j == 0:
                        print(i, end=' ')
                    elif j == coluna_peça:
                        if i == linha_peça:
                            print('o', end=' ')
                        elif i == linha_peça + 1:
                            print('x', end=' ')
                        elif i == linha_peça - 1:
                            print('x', end=' ')
                        else:
                            print('-', end=' ')
                    elif abs(j - coluna_peça) == abs(i - linha_peça) == 1:
                        print('x', end=' ') 
                    elif i == linha_peça:
                        if j == coluna_peça + 1:
                            print('x', end=' ')
                        elif j == coluna_peça - 1:
                            print('x', end=' ')
                        else:
                            print('-', end=' ')
                    else:
                        print('-', end=' ')
                print()   

        elif nome_peça == 'Cavalo':
            print(f'Movimentos para a peca Cavalo a partir da casa {info_peça[1]}{linha_peça}.') 
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if j == 0:
                        print(i, end=' ')
                    elif j == coluna_peça:
                        if i == linha_peça:
                            print('o', end=' ')
                        else:
                            print('-', end=' ')
                    elif abs(j - coluna_peça) == 1:
                        if abs(i - linha_peça) == 2:
                            print('x', end=' ')
                        else:
                            print('-', end=' ')
                    elif abs(j - coluna_peça) == 2:
                        if abs(i - linha_peça) == 1:
                            print('x', end=' ')
                        else:
                            print('-', end=' ')
                    else:
                        print('-', end=' ')
                print()
  
        elif nome_peça == 'Peao':
            print(f'Movimentos para a peca Peao a partir da casa {info_peça[1]}{linha_peça}.') 
            for i in range(dimensao_tabuleiro, 0, -1):
                for j in range(dimensao_tabuleiro + 1):
                    if linha_peça == 2:
                        if j == 0:
                            print(i, end=' ')
                        elif j == coluna_peça:
                            if i == linha_peça:
                                print('o', end=' ')
                            elif j == coluna_peça:
                                if i == linha_peça + 1:
                                    print('x', end=' ')
                                elif i == linha_peça + 2:
                                    print('x', end=' ')
                                else:
                                    print('-', end=' ')
                            else:
                                print('-', end=' ')
                        else:
                            print('-', end=' ')
                    else:
                        if j == 0:
                            print(i, end=' ')
                        elif j == coluna_peça:
                            if i == linha_peça:
                                print('o', end=' ')
                            elif i == linha_peça + 1:
                                print('x', end=' ')
                            else:
                                print('-', end=' ')
                        else:
                            print('-', end=' ')
                print()
        print(' ',end='')
        for i in range(dimensao_tabuleiro):
            print(' '+ chr(ord('a')+i), end='')
        print('\n')
    else:
        break           
