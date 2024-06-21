#Palete Color
color = {'blue':'\033[1;34m',
         'purple':'\033[1;35m',
         'green':'\033[1;32m',
         'yellow':'\033[1;33m',
         'gray':'\033[1;37m',
         'clean':'\033[m'}
print('\n',' '*27,'{}Somando números inteiros {} --> PARES <-- {}\n'.format(color['purple'],color['blue'],color['clean']))
s = 0
cont = 0
print('{}Digite seis valores {} iremos somar apenas NÚMEROS PARES:{}'.format(color['gray'],color['blue'],color['green']))
print('{}'.format(color['clean']))
for c in range(1, 7):
    choice = int(input('\nvalor {} : ---> ' .format(c)))   
    if choice % 2 == 0:
        s = s + choice
        print('{}---> O número acima é {}PAR{} <---{}'.format(color['purple'],color['blue'],color['purple'],color['clean']))
        cont = cont + 1
print()
print('{}Você digitou {}{}{} números {}PARES{}.\n'.format(color['gray'],color['green'],cont,color['clean'],color['blue'],color['clean']))
print('{} Somando os números {}PARES{}: {}{}{}\n'.format(color['yellow'],color['blue'],color['yellow'],color['green'],s,color['clean']))
print()


