print('Detectando números primos')

number = int(input('Informe um número: '))

for c in range(number, 0, -1):
    if number % c == 0: