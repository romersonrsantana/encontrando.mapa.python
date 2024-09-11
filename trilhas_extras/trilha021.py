print()
print('==ººº'*16)
print(' '*27,'All My Cats')
print('====='*16)

cat_names = []

while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) + '(Or enter nothing to stop.):')

    name = input('>>> ').strip()
    
    if name == '':
        print('Names completed')
        break
    else:
        cat_names = cat_names + [name]
    print('The cat names are: ')

for name in cat_names:
    print(' ' + name)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés, Ao Seu Espírito Santo E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.