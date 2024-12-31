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
                    A) Numbers from 1 to 10 of one and one. 
                    B) Numbers from 10 to 0 of two and two.
                    C) Enter the values.
          
          ''')
    
    choice = str(input('Inform the option: >>> '))

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Sagrado Coração de Jesus Confio e Espero em Vós. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.