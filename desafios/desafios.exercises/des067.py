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
        print(' '*3,f'{number} x {c:^3} = {c*number}')
    
    print('~'*18)

print('\nMultiplication table completed successfully.\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. 