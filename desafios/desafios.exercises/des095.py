print('==='*27)
print(' '*36,'Soccer Player')
print('==='*27)

date_list = list()
player = dict()
gols_list = list()

gols = total_goals = 0

while True:
    player['name'] = str(input(">>> What's soccer player's name? "))
    print()
    games = int(input(f'>>> How many games did {player["name"]} play? '))
    print()
    print('---'*27)
    for c in range(0, games):
        gols = int(input(f'--> How many goals did {player["name"]} make in the {c + 1}° game? '))
        gols_list.append(gols)
        
        player['goals'] = gols_list[:]

        #player.setdefault('total_goals', 0)
        #player['total_goals'] += gols
        total_goals += gols
        player['total_goals'] = total_goals
    total_goals = 0
    print('---'*27)
    print()
    gols_list.clear()
    date_list.append(player.copy())

    print('*--*'*18)
    print()
    choise = str(input('>>> Do you want to continue? (y - yes or n - not)? ')).lower()[0]

    if choise in 'n':
        break
    
print('---'*27)
print('Cod.'.ljust(9,' '), end='')
print(' Name '.ljust(18,' '), end='')
print(' Goals '.ljust(16,' '), end='')
print('Total')

for indice, dados in enumerate(date_list): 
    print(f'{indice} ',end='')
    for k, v in dados.items():  
        print(f'{v}'.center(18,' '), end='')
    print()

while True:
    print('==='*27)
    choise_II = int(input('>>> Do you want to see details of player?(Enter the code or enter 999 to exit.) \n\n--> '))

    if choise_II == 999:
        print('¨¨¨'*27)
        print(' '*36,'Program closed!')
        print('¨¨¨'*27)
        print()
        break
    else:
        print('---'*27)
        for c in date_list[choise_II]:
            if 'goals' == c:
                for num, i in enumerate(date_list[choise_II]['goals']):
                    print(f'>>> In the {num+1}st game, {date_list[choise_II]['name']}: {i} goals.')
        print('---'*27)
        print()
       
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Único Filho Nosso Senhor Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.