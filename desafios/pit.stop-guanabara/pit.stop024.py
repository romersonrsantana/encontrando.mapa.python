print('==='*27)
print(' '*36,'Groups')
print('==='*27)

numbers = [[], []]

for c in range(1,8):
    item = int(input(f'> Enter a {c}st number --> '))
    if item % 2 == 0:
        numbers[0].append(item)
    else:
        numbers[1].append(item)

numbers[0].sort()
numbers[1].sort()

print('---'*27)
print(f'>>> The numbers even are: {numbers[0]}.\n')
print(f'>>> The numbers odd are: {numbers[1]}.')
print('---'*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.