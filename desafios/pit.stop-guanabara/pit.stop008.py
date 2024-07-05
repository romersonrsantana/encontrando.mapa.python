print('\n',' '*27,'Detectando números primos\n')

number = int(input('Informe um número: '))
print()
total = 0
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[1;34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')

print('\n\n\033[mO número {} foi dividido {} vezes'.format(number, total))

if total == 2:
    print('\nE por isso ele é PRIMO!\n')
else:
    print('\nE por isso ele NÃO É PRIMO!\n')
    