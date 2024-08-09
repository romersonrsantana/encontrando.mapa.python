colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'alert':'\033[1;31m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

print('\n',' '*27,'{}Arithmetic progression with ten terms{}\n'.format(colors['purple'], colors['clean']))

numero_inicial = int(input('\n{}Enter a number to start the arithmetic progression-->{} '.format(colors['gray'], colors['blue'])))

razao_pa = int(input('\n{}Enter a number that will be the reason for arithmetic programming-->{} '.format(colors['gray'], colors['blue'])))

controle = 0

print()

while controle < 10:
    controle += 1

    if controle == 1:
        total = numero_inicial
        print(f'{colors["purple"]}',total , ' - ' ,end='')
    
    elif controle == 10:
        total += razao_pa
        (print(total, '.' , end=''))

    else:
        total += razao_pa
        print(total ,' - ',end='')

print(f'{colors["clean"]}\n')

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.