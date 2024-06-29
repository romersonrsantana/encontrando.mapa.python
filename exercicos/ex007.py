print('Descobrindo números primos')

choice = int(input('Escolha um número inteiro: '))

for c in range(1, choice + 1):
    if choice / c == 0:
        print(c,'\033[1;35m', end='')
    else:
        print(c,'\033[1;34m', end='')