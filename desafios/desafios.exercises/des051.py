from time import sleep
#Palete Color
color = {'blue':'\033[1;29;44m',
         'purple':'\033[1;29;45m',
         'green':'\033[1;32m',
         'yellow':'\033[1;33m',
         'gray':'\033[1;37m',
         'clean':'\033[m'}

print('\n',' '*27,'{} Progressão Aritmética {}'.format(color['purple'], color['clean']))

first = int(input('\n{}Digite um número inteiro que será o primeiro termo de uma P.A: ---> {}  '.format(color['gray'],color['blue'])))

reason = int(input('\n{}{}Informe um {}número inteiro{} que será a razão da P.A ---> {}  '.format(color['clean'],color['gray'], color['green'], color['gray'], color['blue'])))
print('{}'.format(color['clean']))
sleep(0.7)
print('{}Calculando os {}10 primeiros termos{} dessa P.A{}\n'.format(color['gray'], color['yellow'], color['gray'], color['clean']))
print()
sleep(1.6)
twentieth = first + reason*9

for c in range(first, twentieth + 1, reason):
    print(c,'-', end=' ')
print()
print('\n',' '*18,'{}  Progressão Aritmética concluida com sucesso!!  {}\n'.format(color['blue'],color['clean']))