import random
print('==='*27)
print(' '*36, 'Playing')
print('==='*27)

player = dict()
bigger = list()
game_players = list()

for c in range(0, 4):
    player['name'] = str(input(f'>>> Enter a name for the player {c + 1} --> '))
    print()
    game_players.append(player.copy())

control = 0

for c in game_players:
    for k, v in c.items():
        print(f'--> {control:-^9}: {k} = {v}')
        print()
    control += 1
        
for c in range(0,4):

    number = int(input('Choose the corresponding number for the player to start, \n\n >>> Who is the player to roll the dice? '))

    print('---'*27)
    print(f'\nWell... {c+1}st play...\n')
    print('---'*27)

    if number == 0:
        game_players[0]["dice"] = random.randint(1,6)
    elif number == 1:
        game_players[1]["dice"] = random.randint(1,6)
    elif number == 2:
        game_players[2]["dice"] = random.randint(1,6)
    else:
        game_players[3]["dice"] = random.randint(1,6)
        

controle = 0
while len(game_players) > controle:

    if controle == 0:
        bigger.append(game_players[0].copy())
    else:
        if bigger[0]["dice"] < game_players[controle]["dice"]:
            del bigger[0]
            bigger.append(game_players[controle].copy())

        if bigger[0] == game_players[controle]["dice"]:
            bigger.append(game_players[controle].copy())
    
    controle += 1
print('***'*27)
print(f'\n>>> Total players: {game_players}\n')
print(f'\n>>> The winning player was: {bigger}\n')
print('***'*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.