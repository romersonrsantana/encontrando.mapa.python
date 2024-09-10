print()
print('==='*27,'\n',' '*27,'Football table (brazilian)')
print('==='*27)

position = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Internacional', 'Bragantino', 'Atletico-PR', 'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-GO')

your_team = 0

while True:
    print(
    '''
    inter the corresponding number
    
    [1] The top five in the table.      [4] Search your team. 
    
    [2] The last four in the table.     [5] Exit
    
    [3] All teams in alphabetical order.   '''
)
    try:
        choice = int(input('\nEnter your choice: --> '))
    except:
        for c in range(1,3):
            print('\n[Alert] Enter a value between 1 and 6.\n')
            if c == 3:
                print('You entered incorrect values three times. The program has been terminated.')
                exit()
            else:
                continue
    
    if choice == 1:
        print()
        print('The top five in the table are: ')
        print('---'*27)
        print(position[:6])

    elif choice == 2:
        print()
        print('The last four in the table are: ')
        print('---'*27)
        print(position[-4:])

    elif choice == 3:
        print()
        print('The teams in alphabetical order are: ')
        print('---'*27)
        print(sorted(position))
    
    elif choice == 4:
         
            for c in range(1, 4):
                print()
                your_team = str(input('write your team: --> ')).strip().title()
                print('---'*27)

                try:
                    print(f'Your team {your_team} is in ',position.index(your_team) + 1,'° position.')
                    #print(c) --> Quando break o contador é reiniciado.
                    break
                
                except:
                    print('[Alert] Your team has not been identified, make sure the name has been written correctly and that it is part of the series A table.')

                    if c == 3:
                        print('---'*27)
                        print('[Program closed]\n\nYou entered the name of the wrong club three times, make sure the name was spelled correctly (with accents), that the team belongs to Serie A.')
                        print('---'*27)
                        exit()

    elif choice == 5:
        print('\nProgram ended sucessfully.\n')
        print('---'*27)
        exit()

    else:
        print('[Alert] Enter values between one and five!')
        print('---'*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés Ao Seu Espiríto Santo E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém. 