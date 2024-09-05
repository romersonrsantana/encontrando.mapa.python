print('==='*27)
print(' '*27,'Numbers')
print('==='*27)

n = n1 = 0

def collatz(number):
    if number % 2 == 0:
        return number // 2

    else:
        return 3*number + 1
for attempt in range(1,6):
    try:  
        n = collatz(int(input('Enter a inter number:\n\n --> ')))
        print(n)
    except:
        print(f'\n[Alert] Enter a value!\n\n--> {attempt}st attempt!')

        if attempt == 3:
            print('\nYou made a mistake 3 times!\n\nProgram closed!\n')
            exit()
        else:
            continue

    while n != 1:
        n = collatz(n)
        print(n)
    
    if n == 1:
        print('\nLoop closed!\n')
        break
 
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.