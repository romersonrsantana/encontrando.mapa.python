print('---'*27)
print(' '*36, 'Data history')
print('---'*27)

people = dict()
person = dict()
people_list = list()
control = 1

while True:
    print()
    person[f'name {control}'] = str(input('>>> Enter a Name: '))
    print()
    person[f'sexo {control}'] = str(input('>>> Write the sexo (M - masculino or F - feminino) '))
    print()
    person[f'age {control}'] = int(input(f">>> Enter the {person[f'name {control}']}'s age "))

    control += 1

    people_list.append(person.copy())
    person.clear()

    choise = str(input('>>> Do you to continue? (y - yes or n - not) ')).lower()[0]

    if choise == 'n':
        break

print(people_list)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.