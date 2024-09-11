import random
print()
print('==='*27)
print(' '*27,'Generating random numbers in tuples')

choise = (random.randint(1, 16), random.randint(1, 28), random.randint(1, 34), random.randint(1, 37), random.randint(1, 111))

for c in range(len(choise)):
    if c == 0:
        smaller = choise[c]
        biggest = choise[c]
    else:
        if choise[c] < smaller:
            smaller = choise[c]

        elif biggest < choise[c]:
            biggest = choise[c]

print(choise)

print(f'\nThe smaller number is in position {choise.index(smaller)}, with the value of {smaller:-^18}.')

print(f'\nThe biggest number is in position {choise.index(biggest)}, with the value of {biggest:-^18}.\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés, Ao Seu Espiríto Santo E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.