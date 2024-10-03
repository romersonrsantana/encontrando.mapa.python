print('==='*27)
print(' '*27, 'Resolução Guanabara')
print('==='*27)

lista = []

for c in range(0, 5):
    
    number = int(input('Enter a number: --> '))

    if c == 0:
        lista.append(number)
        print(f'The number has been added position {c}.')

    elif number >= lista[-1]:
        lista.append(number)
        print(f'The number has been added position {len(lista)-1}')

    else:
        control = 0

        while control < len(lista):

            if number <= lista[control]:
                lista.insert(control, number)
                print(f'The number has been added position {control}.')
                break  
            control += 1

print(lista)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.