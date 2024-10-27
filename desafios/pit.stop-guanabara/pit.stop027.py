from random import randint
from time import sleep
from operator import itemgetter

print('==='*27)
print(' '*36, 'Prize draw')
print('==='*27)

games_players = {'jogador_1': randint(1, 6),
                 'jogador_2': randint(1, 6),
                 'jogador_3': randint(1, 6),
                 'jogador_4': randint(1, 6)}
rankin = dict()
control = 1

print()
print(' '*36,'Given rolled by players')

for k, v in games_players.items():
    print()
    print(f'>>> {k} : number of the given {v}')
    sleep(0.9)

print()
print('---'*9, ' Ranking ', '---'*9)

rankin = sorted(games_players.items(), key=itemgetter(1), reverse=True )

for k, v in rankin:
    print()
    print(f'--> The {control}° position: {k} whith the value {v}. ')

    control += 1
print()

print(rankin)

print()

for i, v in enumerate(rankin):
    print(f'>>> The {i+1}° position : {v[0]} with {v[1]} points.')

print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.