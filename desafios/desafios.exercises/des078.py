print('---'*27)
print(' '*27, 'Identifying values')
print('---'*27)

#chamada de função
def basis():
    print('~~~'*27)
    print('The list is formed by:')

    for c in numbers:
        print(f'{c} ', end='')

    print()
    print('~~~'*27)

def verification(test):
    for c in range(len(numbers)):
        if numbers[c] == test:
            print(c,' ... ', end='')
    print()
    print('---'*27)

#controle de variáveis
numbers = []
position = []
position_min = []
control = max = min = 0
equal_max = equal_min = 1

while control < 7:
    print(f'\nTo position {control:-^18}\n')
    try:
        numbers.append(int(input('\nEnter a number:\n\n--> '))) 
    except:
        print('\nEnter a valid value.\n')
        continue  

    if control == 0:
        max = numbers[control]
        pos_max = control
        
        min = numbers[control]
        pos_min = control
    else:
        if max < numbers[control]:
            max = numbers[control]
            pos_max = control

        if min > numbers[control]:
            min = numbers[control]
            pos_min = control
    
    control += 1

basis()

#informações analisadas

print(f'--> Max: {max}, Position... ', end='')

"""for c in range(len(numbers)):
    if numbers[c] == max:
        print(c, ' ... ', end='')
print()
print('---'*27)"""
verification(max)

print(f'--> Min: {min}, Position... ', end='')

"""for c in range(len(numbers)):
    if numbers[c] == min:
        print(c,' ... ', end='')"""
verification(min)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.