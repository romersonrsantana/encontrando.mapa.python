from random import randint
print('==='*27)
print(' '*27,'Random numbers')
print('==='*27)

guess = list()
guess_total = list()
cont = 0

print('\nAt each start, lists will be created with 6 random numbers.\n')

sequence_numbers = int(input('How many random sequences with 6 numbers do you want? '))

while sequence_numbers > cont:
    for c in range(0, 6): 
        number = randint(1, 60)

        if c == 0:
            guess.append(number)

        else:
            control = 0
            while len(guess) > control:
                if guess[control] == number:
                    number = randint(1, 60)
                    guess.append(number)
                    break
                control += 1
            else:
                guess.append(number)
                        
    guess.sort()
    cont +=1
    print(f'Guess {cont} --> {guess}.')
    guess.clear()
    
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.