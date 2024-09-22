print('---'*27)
print(' '*27, 'Database')
print('---'*27)

number = control = choise = 0
numbers_list = []
boolean = False

while boolean != True:

    try:
        number = int(input('Enter a number: --> '))
    except:
        print('Enter a value number!')
        continue

    if number in numbers_list:
        print('Value not accepted!')
    else:
        numbers_list.append(number)
    
    choise = str(input('Do you want to continue?(Y-yes / N-not)')).lower()[0]

    while True:
        if choise == 'n':
            print('Program closed!')
            boolean = True
            break
        elif choise == 'y':
            break
        else:
            print("Enter 'y' or 'n' ")

print(numbers_list)
    
    



#te Amo Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés, te Amo Espírito Santo, te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.