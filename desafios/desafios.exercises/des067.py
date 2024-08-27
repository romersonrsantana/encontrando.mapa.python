print('\n',' '*27,'Multiplication table\n')

while True:
    try:
        number = int(input('\nEnter a number (or enter a negative number to end.):\n\n--> '))
        if number < 0:
            break
    except:
        print("\n[Alert!] You didn't enter a whole number!\n")
        continue

    print('~'*18)

    for c in range(0, 11):
        print(' '*3,f'{c:^3} x {number} = {c*number}')
    
    print('~'*18)

print('\nMultiplication table completed successfully.\n')
