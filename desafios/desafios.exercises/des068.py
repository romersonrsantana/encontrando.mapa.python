from time import sleep
from random import randint

print(f"{' '*27}\nLet's Go to play?")
sleep(2.1)
print(f"\n{' '*27}--> Pair", end='')
sleep(2.1)
print(f"{' '*27}--> Odd\n")

computer = 0
choice_player = 0
sum = 0
counter = 0

while True:
    
    while True:
        try:
            player = int(input('\nChoose [1] for odd or [2] for pair:\n\n--> '))

            if player < 1 or player > 2:
                print('\nAccepted values [1] for odd or [2] for pair!\n')
            else:
                break
        except:
            print('\n[ERROR] Inform accepted values!\n')
            continue

    computer = randint(1, 1000000)

    while True:
        try:
            choice_player = int(input('\nChoose a number:\n\n-->'))
            if choice_player < 0 or choice_player >= 0:
                break
        except:
            print('\n[ERROR] Enter an integer!\n')
            continue

    sum = computer + choice_player

    print(f'\nThe computer chose the number: --> {computer}.\n\nYou chose the number: --> {choice_player}.')

    if sum % 2 == 0 and player == 2:
        print('\nThe result is par!\n\nCongratulations!!\n')
    elif sum % 2 != 0 and player == 1:
        print('\nThe result is odd!\n\nCongratulations!!\n')
    else:
        print('\nYou Lost!!\n')
        break

    counter += 1

print(f'\nYou won {counter} times!\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.