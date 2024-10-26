import random
import time

print('==='*27)
print(' '*36,'Dice Game')
print('==='*27)


game_playes = list()

control = 1


for c in range(0, 6):

    player = dict()

    player[f'person{c}'] = random.randint(1, 6)

    game_playes.append(player.copy())

    print(f'The player {c+1} : Tirou {player[f"person{c}"]}')
    del player[f'person{c}']
print()

control = 0
biggest = list()

for c in game_playes:
    for v in c.values():
        if control == 0:
            biggest.append(c.items())

        else:
            if biggest[0][f'person{control}'] < c.values():
                biggest.insert(c, 0)
            elif biggest[-1][f'person{control}'] > c.values():
                biggest.insert(c, 1)
            else:
                biggest.append(c)

        #control += 1
            
print(f'Dice {game_playes}')

print(f'{biggest}')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.