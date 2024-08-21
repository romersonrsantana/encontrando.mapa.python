colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'yellow':'\033[1;33m',
          'green':'\033[1;32m',
          'alert':'\033[1;31m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

print('\n',' '*27,f'{colors["purple"]}Testando números{colors["clean"]}\n')

escolha_usuario = 0

while True:
    try:
        primeira_escolha = float(input('\nDigite o {}primeiro valor{} númerico: -->{} '.format(colors['green'],colors['clean'],colors['blue'])))
        print(f'{colors["clean"]}')
        break     
    except:
        print(f'\n{colors["alert"]}[ERRO]{colors["gray"]} Informe um valor númerico.{colors["clean"]}')
        continue

while True:
    try:
        segunda_escolha = float(input('Digite o {}segundo valor{} númerico: -->{} '.format(colors['yellow'],colors['clean'],colors['blue'])))
        print(f'{colors["clean"]}')
        break
    except:
        print(f'\n{colors["alert"]}[ERRO]{colors["gray"]} Informe um valor númerico.{colors["clean"]}')
        continue

while escolha_usuario != 5:
    print(f'''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
          
    {colors["blue"]}Escolha uma das opções que indique o que deverá ser feito com os valores indicados:{colors["clean"]} ''') 
    try:
        escolha_usuario = int(input(f'-->{colors["blue"]} '))
        print(f'{colors["clean"]}')
    except:
        print(f'\n{colors["alert"]}[ERRO]{colors["gray"]} Informe um valor válido!{colors["clean"]}\n')
        continue

    if escolha_usuario == 1:

        print(f'\n{colors["purple"]}Somando os valores{colors["clean"]} {primeira_escolha} + {segunda_escolha} = ', primeira_escolha + segunda_escolha)

    elif escolha_usuario == 2:

        print(f'\n{colors["purple"]}Multiplicando os valores{colors["clean"]} {primeira_escolha} x {segunda_escolha} = ', primeira_escolha * segunda_escolha)
    
    elif escolha_usuario == 3:
      if primeira_escolha > segunda_escolha:
          print(f'\n {colors["purple"]}O maior valor é{colors["clean"]} {primeira_escolha} !')

      elif segunda_escolha > primeira_escolha:
          print(f'\n {colors["purple"]}O maior valor é{colors["clean"]} {segunda_escolha} !')

      else:
          print(f'\n{colors["alert"]}Ambos os valores são iguais!!{colors["clean"]}')

    elif escolha_usuario == 4:
        print(f'\n{colors["blue"]}Novos valores!{colors["clean"]}\n')
        while True:
            try:
                primeira_escolha = float(input(f'Primeiro valor -->{colors["blue"]} '))
                print(f'{colors["clean"]}')
                break
            except:
                print(f'\n{colors["alert"]}[ERRO]{colors["gray"]} Informe valores númericos!{colors["clean"]}')
                continue
        while True:
            try:
                segunda_escolha = float(input('Segundo valor -->{} '.format(colors['blue'])))
                print(f'{colors["clean"]}')
                break
            except:
                print(f'\n{colors["alert"]}[ERRO]{colors["gray"]} Informe valores númericos!{colors["clean"]}\n')
                continue
       
    elif escolha_usuario == 5:
        print(f'\n{colors["purple"]}Programa encerrado com sucesso!{colors["clean"]}\n')
    
    else:
        print('\n{}[Alert]{} Escolha somente as opções válidas!{}\n'.format(colors["alert"],colors["gray"],colors["clean"]))

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. E também Toda Honra e Glória Ao Espirito Santo e ao Nosso Senhor Jesus Cristo. Amém.