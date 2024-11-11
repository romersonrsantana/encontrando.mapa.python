print('==='*27)
print(' '*36,'Soccer Player')
print('==='*27)

date_list = list()
player = dict()
gols_list = list()

gols = total_goals = 0

while True:
    player['name'] = str(input("What's soccer player's name? "))
    player['games'] = int(input(f'How many games did {player["name"]} play? '))

    for c in range(0, player['games']):
        gols = int(input(f'How many goals did {player["name"]} make in the {c + 1}° game? '))
        gols_list.append(gols)

        player.setdefault('total_goals', 0)
        player['total_goals'] += gols
    
    player['goals'] = gols_list[:]
    gols_list.clear()
    date_list.append(player.copy())

    choise = str(input('>>> Do you want to continue? (y - yes or n - not) ? ')).lower()[0]

    if choise in 'n':
        break
    
print('---'*27)
print(' Cod. '.ljust(9,' '), end='')
print(' Name '.ljust(18,' '), end='')
print(' Goals '.ljust(9,' '), end='')
print('Total')

for c in date_list:
    for k, v in c.items():

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Único Filho Nosso Senhor Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.