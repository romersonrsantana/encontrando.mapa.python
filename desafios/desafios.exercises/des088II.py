from random import randint
print('==='*27)
print(' '*27, 'Random Numbers')
print('==='*27)

start = 1
the = 10

aleatorio = list()

for c in range(0, 6):
    aleatorio.append(randint(start, the))
    start += 10
    the += 10
    print(f'{start} --> {the}')
    print(aleatorio)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.