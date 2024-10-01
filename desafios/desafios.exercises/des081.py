print('==='*27)
print(' '*27,'Analyzing values')
print('==='*27)

boolean = False
control = 0
list_numbers = []

#--------------------- start of function call ------------------
def art():
    print('---'*27)

def choise_search(number_2): #verifica se o número informado está na lista
    art()
    if number_2 in list_numbers:
        print(f'--> The number {number_2:.^9} is in the list, in the posicion {list_numbers.index(number_2):.^9}')
    else:
        print(f'The number {number_2:.^9} is not find.')
    art()

def to_be(): #continuação ou encerramento do program 
    while True:
        search = str(input('Do you want to find another number in the list? [Y - yes or N - no]\n--> ')).lower()[0]

        if search == 'y':
            break
        elif search == 'n':
            print('Program completed successfully!')
            exit()
            break
        else:
            print('[Alert] Enter Y or N.')

#-------------------- end of function call ----------------------

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

#----------- start conclusion of the reported data -------------
art()
print('Values inserted into the list according to the insertion order: \n--> ',list_numbers)
art()
print(f'--> Total of the numbers {control}')
art()
print(f'--> Numbers in descending order ', end='')
list_numbers.sort(reverse=True)
print(list_numbers)
art()
if 5 in list_numbers:
    print('--> Há o número 5 na lista, a primeira incidencia acontece na posição ', end='')
    print(f'{list_numbers.index(5)}')
else:
    print('--> Não foi encontrado o valor 5 na lista.')
art()
print()

#----------------- end conclusion of the reported data --------

boolean = False

while boolean != True: #loop para busca de valores in the list

    to_be()

    try:
        number_choise = int(input('Enter a number to search in the list: --> '))
    except:
        print('[ERRO] Enter a valid value.')
        continue

    choise_search(number_choise)

#Te Amo Pai Celestial Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés. Te Amo Espírito Santo. Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.