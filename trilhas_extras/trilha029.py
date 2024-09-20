print('---'*27)
print(' '*27,'Birthday database')
print('---'*27)

birthdays = {'Tereza': 'December, 16th ', 'João': 'March, 28th', 'Renan':'March, 03th', 'Robson':'february, 11th', 'Enzo':'July, 02th'}

while True:
    name = (str(input('\nEnter a name (or enter to exit): --> '))).strip().title()

    if name == '':
        break
    
    if name in birthdays:
        print('\n',birthdays[name] + ' is of the Birthday of ' + name)
    
    else:
        print('\n','I do not have birthday information for ', name, '\n\nWhat is their birthday? ')

        new_name = str(input('>>> '))

        birthdays[name] = new_name

        if new_name == '':
            print('\nClosed program!\n')
            exit()

        print('\n','Birthday database updated.')
        
        print('\n','==='*27)
        print(birthdays)
        print('\n','==='*27)

#te Amo Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés, te Amo Espírito Santo, te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.