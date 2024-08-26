print('\nMultiplication table!\n')

while True:
    try:
        number = int(input('\nEnter an interger:\n\n--> '))
        if number >= 0:
            break
    except:
        print('\n[Alert] Enter a valid number!\n')
    continue

