import random
import time
from operator import itemgetter

print('==='*27)
print(' '*36,'Dice Game')
print('==='*27)


game_playes = list()
raking = dict()
control = 1


for c in range(0, 4):

    player = dict()

    player[f'person{c}'] = random.randint(1, 6)

    game_playes.append(player.copy())

    print(f'The player {c+1} : Tirou {player[f"person{c}"]}')
    time.sleep(1)

    del player[f'person{c}']
print()

'''for c in range(0, len(game_playes)):
    raking = sorted(game_playes[c]player.items(), key=itemgetter(1))'''

#Foi feito um dicionário para cada item dentro da lista.

print(game_playes)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.