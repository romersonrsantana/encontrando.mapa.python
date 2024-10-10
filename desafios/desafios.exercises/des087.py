print('==='*27)
print(' '*27, 'Estrutura de Dados')
print('==='*27)

numbers = list()
number_line = list()
control = total = 0

while control <= 2:

    for c in range(0, 3):

        number_line.append(int(input(f'Enter a number for the [{control}, {c}] --> ')))
    
    numbers.append(number_line[:])
    number_line.clear()
    control += 1

print('---'*27)
control = 0
for c, value in enumerate(numbers):

    for uni, item in enumerate(value):

        if item % 2 == 0:
            total += item

        if uni == 2 or uni == 5:
            print(f'[ {item:^9} ]')
        else:
            print(f'[ {item:^9} ]', end='')
print('---'*27)

print(f'>>> Adding even values {total}.')
print(f'>>> Adding the values in the third column {numbers[0][2] + numbers[1][2] + numbers[2][2]}')
print(f'>>> The max number is {max(numbers[1]):-^9}')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.