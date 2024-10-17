print('---'*27)
print(' '*36,'Basedate')
print('---'*27)

base_date = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

total = sum_third = bigger = smaller = 0

for colun in range(0, 3):
    for line in range(0, 3):
        base_date [colun][line] = int(input(f'\n>>> Enter a number in the position [{colun}, {line}]: '))

        if base_date[colun][line] % 2 == 0:
            total += base_date[colun][line]

print()
for colun in range(0, 3):
    for line in range(0, 3):
        print(f'...{base_date[colun][line]:^9}... ', end='')
    print()

for c in range(0, 3):
    sum_third += base_date[c][2]

for line in range(0, 3):
    if line == 0:
        bigger = base_date[1][line]
    else:
        if bigger < base_date[1][line]:
            bigger = base_date[1][line]

print()
print('~~~'*27)
print(f'\n--> The total sum of even numbers is: {total}.')
print(f'\n--> Total of the values in the third column {sum_third}.')
print(f'\n---> The bigger value in the second line is {bigger}.')
print()
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.