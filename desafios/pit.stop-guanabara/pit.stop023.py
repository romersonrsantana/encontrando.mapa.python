print('==='*27)
print(' '*36,'Base date')
print('==='*27)

person = list()
base_date = list()
bigger = smaller = 0

while True:
    person.append(str(input(f'\nEnter a {len(base_date) + 1 }st name --> ')))
    person.append(float(input(f"\nEnter a {person[0]}'s weight --> ")))

    if len(base_date) == 0:
        bigger = smaller = person[1]
    else:
        if bigger < person[1]:
            bigger = person[1]

        if smaller > person[1]:
            smaller = person[1]
    
    base_date.append(person[:])
    person.clear()

    print()
    print('---'*27)
    choise = str(input('Do you want to continue? [Y - yes or N - not] >>> '))

    if choise in 'Nn':
        break
print()
print('~~~'*27)
print(f'--> {len(base_date)} people were registered. \n')
print(f'--> The bigger weight was of {bigger}kg of the people: ', end='')
for c in base_date:
    if c[1] == bigger:
        print(f'{c[0]}... ', end='')
print()
print(f'--> The smaller weight was of {smaller}kg of the people: ', end='')
for JC in base_date:
    if JC[1] == smaller:
        print(f'{JC[0]}... ', end='')
print()
print('~~~'*27)
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.