print('==='*27)
print(' '*27,'Number separator')
print('==='*27)

list_even = [] #par
list_odd = []  #impar
list_total = []
boolean = False

while boolean != True:

    while True:
        try:
            number = int(input('Enter a number: --> '))
            break
        except:
            print('[Alert] Enter a valid value!')
        continue
        
    list_total.append(number)
     
    while True:
        choice = str(input('Do you want to continue? [y - yes or n - no]\n\n--> ')).lower()[0]

        if choice == 'y':
            break
        elif choice == 'n':
            boolean = True
            break
        else:
            print("Enter 'y' or 'n'")

for c in range(len(list_total)):
    if list_total[c] % 2 == 0:
        list_even.append(list_total[c])
    else:
        list_odd.append(list_total[c])

print('---'*27)
print('--> Total List: ',list_total,'\n')
print('--> Even List: ',list_even,'\n')
print('--> Odd List: ',list_odd)
print('---'*27)



#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.