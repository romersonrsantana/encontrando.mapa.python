print('---'*27)
print(' '*27, 'Database')
print('---'*27)

number = control = choise = 0
numbers_list = []
boolean = False

while boolean != True:

    control += 1

    try:
        number = int(input(f'{control:-^9} Enter a number: --> '))
    except:
        print('\n[ERRO!] Enter a value number!\n')
        continue

    if number in numbers_list:
        print('\n[Alert!] Value not accepted!\n', f'O número {number:.^9} já está na lista na posição: ',numbers_list.index(number))
        
    else:
        numbers_list.append(number)
    
    while True:

        print('==='*27)
        choise = str(input('Do you want to continue?(Y-yes / N-not)\n--> ')).lower()[0]

        if choise == 'n':
            print('\nProgram closed!')
            print('---'*27)
            boolean = True
            break
        elif choise == 'y':
            break
        else:
            print("\n[Alert]Enter 'y' or 'n' ")

print('\nlista informada em ordem crescente: ',sorted(numbers_list))
print()
    

#te Amo Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés, te Amo Espírito Santo, te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.