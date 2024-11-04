print('==='*27)
print(' '*36, 'Control')
print('==='*27)

play_soccer = dict()
gols_numbers = dict()

play_soccer['name'] = str(input('Enter a name of the soccer play: --> '))

play_soccer['number of games'] = int(input(f'How many games did {play_soccer["name"]} play: --> '))

for c in range(1, play_soccer['number of games'] + 1):
    print()
    gols_numbers[f'In game {c}'] = int(input(f'How many were scored: (game {c}) --> '))

play_soccer['goals scored'] = 0

for v in gols_numbers.values():

    play_soccer['goals scored'] += v

play_soccer['game days'] = gols_numbers.copy()

print('---'*27)
for k, v in play_soccer.items():
    print()
    print(f'>>> {k} : {v}')

print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.