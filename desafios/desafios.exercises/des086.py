print('==='*27)
print(' '*36,'Matrix')
print('==='*27)

values = list()

for c in range(0, 9):
    values.append(int(input(f'\nEnter an integer {c:.>6} : --> ')))

for c, v in enumerate(values):
    if c < 2:
        print(f' {v} |', end='')
    elif c == 2:
        print(f' {v} |')
        print('---'*6)
    elif c < 5:
        print(f' {v} |', end='')
    elif c == 5:
        print(f' {v} |')
        print( '---'*6)
    else:
        print(f' {v} |', end='') #fazer 3 lists

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.