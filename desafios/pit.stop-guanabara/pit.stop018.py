print('\n',' '*27,'Fibonacci Sequence\n')

termo_1 = 0
termo_2 = 1
counter = 3

number = int(input('Enter how many terms in the sequence you want to see: \n\n >>> '))
print()

print('{} --> {} --> '.format(termo_1, termo_2), end='')

while counter <= number:

    total = termo_1 + termo_2

    print('{} --> '.format(total), end='')

    termo_1 = termo_2
    termo_2 = total

    counter += 1

print('The end.\n')

#Não compreendo Os Seus Caminhos, mas te darei a minha canção. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.