print('==='*27)
print(' '*27,'Heavy People')

#control list
registered_people = list()
person = list()
bigger = list()
smaller = list()
control = 0

while True:
    print('==='*27)
    person.append(str(input('--> Enter a name of the person: ')))
    print()
    person.append(int(input(f"--> Enter the {person[0]}'s wight: ")))

    registered_people.append(person[:])
    person.clear()

    control +=1
    
    print('---'*27)
    choise = str(input('>>> Do you want to continue? [y - yes or n - not] '))

    if choise == 'n':
        break

print('---'*27)
print(f'Total number of people {control:-^9}')

for indice, valor in enumerate(registered_people):
    if indice == 0:
        bigger.append(valor)
        smaller.append(valor)
    else:
        if bigger[0][1] < registered_people[indice][1]:
            bigger.clear()
            bigger.append(valor)
        elif bigger[0][1] == registered_people[indice][1]:
            bigger.append(valor)
        
        if smaller[0][1] > registered_people[indice][1]:
            smaller.clear()
            smaller.append(valor)
        elif smaller[0][1] == registered_people[indice][1]:
            smaller.append(valor)
        


print(f'The biggest weights are: {bigger}')
print(f'The smallest weights are: {smaller}')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.