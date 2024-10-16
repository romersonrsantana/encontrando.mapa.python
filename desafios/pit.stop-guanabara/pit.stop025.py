print('---'*27)
print(' '*36,'Table')
print('---'*27)

base_date = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0,3):
    for colun in range(0,3):
        base_date[line][colun] = int(input(f'>>> Enter a number [{line}, {colun}]: '))
        print()
    print()

for line in range(0,3):
    for colun in range(0,3):
        print(f'[{base_date[line][colun]:^9}] ',end='')
    print()

print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.