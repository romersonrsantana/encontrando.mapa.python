print('\nTest login\n')

name = input(str('\nWhat is your name? \n\n --> '))

if name == 'Mary':
    print('\nHello Mary!\n')
else:
    print("\nYou aren't Mary!\n")

password = input(str('\nWhat is the password? \n\n --> '))

if password == 'swordfish':
    print('\nAccess granted!\n')
else:
    print('\nWrong password!\n')