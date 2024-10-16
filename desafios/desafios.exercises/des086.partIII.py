print('==='*27)
print(' '*27, 'Vetor')
print('==='*27)

vetor = list()
number_list = list()

control = 0

while control <= 2:

    for c in range(0,3):

        number_list.append(int(input(f'Enter a number for the vector in the position [{control},{c}] --> ')))

        vetor.append(number_list[:])
        number_list.clear()
    
    control += 1

'''for c in range(0, 3):

    number_list.append(int(input(f'Enter a number for the vector in the position [1,{c}] --> ')))

    vetor.append(number_list[:])
    number_list.clear()

for c in range(0, 3):

    number_list.append(int(input(f'Enter a number for the vector in the position [2,{c}] --> ')))

    vetor.append(number_list[:])
    number_list.clear()'''

for c, v in enumerate(vetor):
    if c <= 1:
        print(f' {v} ', end='')
    elif c == 2:
        print(f' {v} ')
    elif c < 5:
        print(f' {v} ', end='')
    elif c == 5:
        print(f' {v} ')
    else:
        print(f' {v} ', end='')
print()

#Te Amo Pai Celestial, Papai do Céu, Deus de Abraão, Isaac, Jacó, Israel e Moisés, Te Amo Espírito Santo, Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.