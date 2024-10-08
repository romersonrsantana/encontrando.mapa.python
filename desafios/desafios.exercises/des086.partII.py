print('==='*27)
print(' '*36,'Matrix')
print('==='*27)

first_line = list()
second_line = list()
third_line = list()

for c in range(0, 9):
    if c <= 2:
        first_line.append(int(input(f'Enter a number in the position [0, {c}] --> ')))
    elif c <= 5:
        second_line.append(int(input(f'Enter a number in the position [1, {c-3}] --> ')))
    else:
        third_line.append(int(input(f'Enter a number in the position [2, {c-6}] --> ')))
print()
print(' '*27,f'{first_line}')
print(' '*27,f'{second_line}')
print(' '*27,f'{third_line}')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.