colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'alert':'\033[1;31m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

print('\n',' '*27,'{}Discovering the factorial{}\n'.format(colors['purple'], colors['clean']))

factorial = 3

while True:
    try:
        usuario = float(input('\n{}Indique um número para iniciar: -->{}  '.format(colors['blue'], colors['gray'])))
        print('{}'.format(colors['clean']))
        break
    except:
        print('\n{}[ALERT]{} Insira valores válidos{}'.format(colors['alert'], colors['gray'], colors['clean']))
        continue

inicio = usuario

while factorial > 1:

    factorial = usuario - 1

    if inicio == usuario:
        total = (inicio * factorial)

        print(usuario, ' x ', end='')
        print(factorial, ' x ', end='')

    elif factorial == 1:
        total = total * factorial

        print(factorial, ' = ', end='')

    else:
        total = total * factorial

        print(factorial, ' x ', end='')
    
    usuario = usuario - 1

print(f'{colors["purple"]}',total,f'{colors["clean"]}')
print('\n')
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espirito Santo. Toda Honra e Toda Glória a Jesus Cristo. Amém. 