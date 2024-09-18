print()
print('¨¨¨¨==='*9)
print(' '*27,'Reading values')
print('======='*9)

test1 = (int(input('\nEnter the first number --> ')))
test2 = (int(input('\nEnter the second number --> ')))
test3 = (int(input('\nEnter the third number --> ')))
test4 = (int(input('\nEnter the fourth number --> ')))

total = ''
control = 0

test = (test1, test2, test3, test4)

for c in range(len(test)):
    if test[c] == 3:
        repeat = test.index(3) + 1
        break
    else:
        repeat = " Didn't appear once "

print()
print('¨¨¨'*27)
print('The numbers reported are ' + str(test) + '.')

print(f'\n>>> The number (9) nine appeared {test.count(9)} times.\n')

print('\n>>> The first time the number (3) three appeared, was in position ' + str(repeat) + '.\n')

print('==='*27)
print(' '*27,'Numbers pairs')
print('==='*27)

for c in range(len(test)):
    if test[c] % 2 == 0:
        print(f'{test[c]} ', end='')

        control += 1

if control == 0:
    print('\nNo even numbers were entered.\n')

print(f'\n',' '*27,'Program completed successfully!\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés, Ao Seu Espírito Santo e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.