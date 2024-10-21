print('==='*27)
print(' '*36, 'Playing')
print('==='*27)

player = dict()
game_players = list()

for c in range(0, 4):
    player['name'] = str(input(f'>>> Enter a name for the player {c + 1} --> '))
    print()
    game_players.append(player.copy())

control = 0

print('Choose the corresponding number for the player to start.')
for c in game_players:
    for k, v in c.items():
        print(f'--> {control:-^9}: {k} = {v}')
    control += 1

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.