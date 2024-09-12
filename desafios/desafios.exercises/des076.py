print('==='*27)
print(' '*27,'TJ Supermarket')
print('==='*27)

price = ('Rice', 28.16, 'Beans', 5.68, 'Sugar', 16.15, 'cooke', 1.75, 'orange', 1.78, 'past', 2.36)

for c in range(len(price)):
    if c % 2 == 0:
        print(f'>>> {price[c]:<9}', '---'*18, end='')
    else:
        print(f' U$ {price[c]:>7}')
print('==='*27)

print('\n\nToda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés \nAo Seu Espírito Santo E Ao Seu Filho Amado Jesus Cristo. \nLouvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.\n')