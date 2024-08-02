print('\nTestando números\n')

palete_colors = {'blue':'\033[1;34m',
                 'purple':'\033[1;35m',
                 'yellow':'\033[1;33m',
                 'green':'\033[1;32m',
                 'alert':'\033[1;31m',
                 'gray':'\033[1;37m',
                 'clean':'\033[m'}

escolha_usuario = 0

while True:
    try:
        primeira_escolha = float(input('\nDigite o primeiro valor númerico: --> '))
        break     
    except:
        print('\n[ERRO]Informe um valor númerico.')
        continue

while True:
    try:
        segunda_escolha = float(input('\nDigite o segundo valor númerico: --> '))
        break
    except:
        print('\n[ERRO]Informe um valor númerico.')
        continue

while escolha_usuario != 5:
    print(f'''
        Primeiro valor --> {primeira_escolha}
        Segundo valor --> {segunda_escolha}

        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
          
    Escolha uma das opções que indique o que deverá ser feito com os valores escolhidos:   
          ''')
    
    escolha_usuario = int(input('\n--> '))

    if escolha_usuario == 1:

        print(f'\nSomando os valores {primeira_escolha} + {segunda_escolha} = ', primeira_escolha + segunda_escolha)

    elif escolha_usuario == 2:

        print(f'\nMultiplicando os valores {primeira_escolha} x {segunda_escolha} = ', primeira_escolha * segunda_escolha)
    
    elif escolha_usuario == 3:
      if primeira_escolha > segunda_escolha:
          print(f'\n O maior valor é {primeira_escolha} !')

      elif segunda_escolha > primeira_escolha:
          print(f'\n O maior valor é {segunda_escolha} !')

      else:
          print('\nAmbos os valores são iguais!!')

    elif escolha_usuario == 4:
        print('\nNovos valores!\n')
        while True:
            try:
                primeira_escolha = float(input('\nPrimeiro valor --> '))
                break
            except:
                print('\n[ERRO] Informe valores númericos!')
                continue
        while True:
            try:
                segunda_escolha = float(input('\nSegundo valor --> '))
                break
            except:
                print('\n[ERRO] Informe valores númericos!\n')
                continue
       
    elif escolha_usuario == 5:
        print('\nPrograma encerrado com sucesso!\n')
    
    else:
        print('\n[Alert] Escolha somente as opções válidas!\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. E também Toda Honra e Glória Ao Espirito Santo e ao Nosso Senhor Jesus Cristo. Amém.