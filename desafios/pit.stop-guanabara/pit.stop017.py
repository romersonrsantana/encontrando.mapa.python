print('\n',' '*27,'Gerador de P.A \n')

start = int(input('Enter a number to start the P.A: --> '))

reason = int(input('\nEnter a number to the reason: --> '))

term = start
control = 1
more_terms = 9
total = 0

while more_terms != 0:
    total += more_terms

    while control <= total:
        print(' {} --> '.format(term), end='')
        control += 1
        term += reason
    print('Pausa.')
    
    more_terms = int(input('\nHow many terms would you like to know?\n\n --> '))

print('\nProgram ended successfully, {} terms werw reported.\n'.format(total))

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.