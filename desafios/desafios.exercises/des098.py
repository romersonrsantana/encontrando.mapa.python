def layout(character, msg):
    print(f'{character}' * 36)
    print(' '*54, f'{msg}')
    print(f'{character}' * 36)

def parameter(start, end, step):
    print('---'*36)
    for c in range(start, end, step):
        print(f'{c} ', end='')
    print()
    print('---'*36)

layout('===', 'Check')
print()

while True:
    print('''
          Choice:
                    A) Numbers from 1 to 12 of one and one. 
                    B) Numbers from 12 to 0 of two and two.
                    C) Enter the value.
                    D) Exit.
          
          ''')
    
    choice = str(input('Inform the option: >>> ')).lower()[0]

    if choice == 'a':
        parameter(1, 12, 1)
    elif choice == 'b':
        parameter(12, 0-1, -1)
    elif choice == 'c':
        one = int(input('       Enter a number to start: >>> '))
        two = int(input('''       
                        Enter a number to finalize: 
            (For countdown enter the highest value followed by the stop value with the step(arithmic radio) 
            **must be a negative number) 
                        >>> '''))
        three = int(input('     Enter a number to step: >>> ')  )
        parameter(one, two, three)
    elif choice == 'd':
        break
    else:
        print()
        print('     [Alert] Please provide correct option.')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Sagrado Coração de Jesus Confio e Espero em Vós. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.