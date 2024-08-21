from random import randint

print('\nGuess the number!\n')

computer = randint(0,12)

palpite = False

contador = 0

while not palpite:
    
    try:
        player = int(input('Enter a number between zero and twelve: '))
    except:
        print('\nYou did not provide acceptable values!\n')
        continue

    contador += 1

    if player == computer:
        palpite = True

    else:
        if player < computer:
            print('\nTry a bigger number!\n')
        elif player > computer:
            print('\nTry a smaller number!\n')

print('\nCongratulations!! You got it right in {} guess(es)\n'.format(contador))

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.