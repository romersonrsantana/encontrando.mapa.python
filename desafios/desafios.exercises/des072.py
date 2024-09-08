print()
print('####'*18)
print(' '*27,'Writing a number')
print('####'*18,'\n')

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

choice = control = next =  0

while True:
    print('---'*27)
    
    try:
        choice = int(input('Enter a number between 0 and 20: \n\n--> '))
    except:
        print('\n[Alert!] Enter an integer, between 0 and 20.\n')
        continue

    if choice < 0 or choice > 20:
        print('\n[Alert] Value not accepted!\n')
    
    else:
        print(f'\nThe number provided corresponds to:\n\n>>> {choice} --> {numbers[choice]}')

        control += 1
    
    next = str(input('\nDo you want inter a number?\n\n[y] yes or [n] no.\n\n>>> ')).lower()[0]

    if next == 'n':
        break

print(f'\nProgram completed successfully!\n\nTotal numbers reported {control:^20}\n')
    
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés Ao seu Espiríto Santo e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.