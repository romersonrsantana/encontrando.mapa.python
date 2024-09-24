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

#controle de variáveis
numbers = []
position = []
position_min = []
control = max = min = 0
equal_max = equal_min = 1

while control < 5:
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

        elif max == numbers[control]:
            position.append(control)
            equal_max += 1

        if min > numbers[control]:
            min = numbers[control]
            pos_min = control

        elif min == numbers[control]:
            position_min.append(control)
            equal_min += 1
    
    control += 1

basis()

#informações analisadas

print(f'--> Max: {max}, Posições {pos_max}... ', end='')

if equal_max > 1:
    for c, d in enumerate(numbers):
        if max in numbers:
            print(numbers[c],'...' , end='')

    print(f'--> There are {equal_max} equal maximum values in the list.\n')

print()
print('---'*27)

print(f'--> Min: {min}, Posições {pos_min}... ', end='')
if equal_min > 1:
    for c in position_min:
        print(c,'...', end='')

    print(f'--> There are {equal_min} equal minimum values in the list.\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.