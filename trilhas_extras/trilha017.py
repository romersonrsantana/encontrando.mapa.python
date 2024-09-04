import random

print('==='*27)
print('\n',' '*27,'You guessed my number?\n')
print('==='*27)

secret_number = random.randint(1, 20) #o valor de retorno será armazenado na variável.
print("\nI'm thinking of a number between 1 and 20.\n")

for guess_taken in range(1,7):
    print(f'\nTake a guess. You have 6 chances. {guess_taken}st attempt\n')

    try:
        guess = int(input('\n--> '))     
    except:
        print('\n[Alert!] Wrong value!\n')
        if guess_taken == 6:
            print('==='*27)
            print('\n',' '*27,'Program closed!\n')
            print('==='*27)
            exit()
        continue
    print('==='*27)

    if guess < secret_number:
        print('\nYour guess is too low!\n')
    elif guess > secret_number:
        print('\nYour guess is too high!\n')
    else:
        break #O palpite correto, interrompe o laço for.

if guess == secret_number:
    print('\nGood Job! You guessed my number in ' + str(guess_taken) + ' guesses!')
    print('==='*27)

else:
    print("\nNope. The number I'm thinking of was " + str(secret_number) + '.\n')
    print('==='*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.