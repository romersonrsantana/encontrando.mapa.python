print('==='*27)
print(' '*36, 'Soccer Player')
print('==='*27)

soccer = dict()
days_soccer = list()

soccer['name'] = str(input('>>> Enter the name of the soccer player: --> '))
soccer['number games'] = int(input('>>> Enter the number of games: --> '))

for c in range(1, soccer['number games'] + 1):
    days_soccer.append(int(input(f'How many goals were scored in game {c}st: --> ')))

soccer['days_soccer'] = days_soccer[:]
soccer['Gols Total'] = sum(days_soccer[:])

print('-=-='*18)
print(soccer)
print('-=-='*18)

for v, k in soccer.items():
    print()
    print(f'>>> The label {v} has the value {k}.')

print('-=-='*18)

print(f'The player {soccer["name"]} it played {soccer["number games"]}.')

for c, v in enumerate(soccer['days_soccer']):
    print(' '*7,f'--> In game {c + 1} the player with {v} goals.')

print(f'It was a total of {soccer["Gols Total"]} goals.')
print()

#Eu Te Amo O Senhor És O Meu Deus e Minha Salvação, Eu Te Amo Espírito Santo, Eu Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.