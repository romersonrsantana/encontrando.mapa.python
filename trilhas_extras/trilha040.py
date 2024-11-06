print('---'*27)
print(' '*36,'How old are you? ')
print('---'*27)

while True:
    print()

    age = str(input('>>> What is your age? '))
    
    print()

    if age.isdecimal() == True and len(age) < 3:
        print('>>> Good!!')
        break
    elif len(age) >= 3:
        print('Se você colocou que sua idade é maior que 100 anos... Você deve ta me zuando!')
    else:
        print('Please enter a number for your age')

print('==='*27)

while True:
    print()
    password = str(input('>>> Select a new password (letters and numbers only) '))
    print()
    if password.isalnum() == True and len(password) < 8:
        print("It's Ok!")
        break
    elif len(password) >= 7:
        print('The password must be up to (7 seven) caracteres long!')
    else:
        print('Passwords can only have letters and numbers')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Amém.