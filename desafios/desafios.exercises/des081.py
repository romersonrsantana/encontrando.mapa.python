print('==='*27)
print(' '*27,'Analyzing values')
print('==='*27)

boolean = False
control = 0
list_numbers = []

while boolean != True:

    while True:
        try:
            number = float(input('Enter a number: '))
            break
        except:
            print('Enter a valid value!')
            continue
    
    while True:
        choise = str(input('Do you want to continue? [Y - yes or N - no]\n\n--> ')).lower()[0]

        if choise == 'y':
            break
        elif choise == 'n':
            boolean = True
            break
        else:
            print("Enter 'y' or 'n'.")
    
    list_numbers.append(number)

    control += 1

print(list_numbers)



#Te Amo Pai Celestial Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés. Te Amo Espírito Santo. Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.