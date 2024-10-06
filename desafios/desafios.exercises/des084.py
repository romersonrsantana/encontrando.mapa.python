print('==='*27)
print(' '*27,'Heavy People')
print('==='*27)

registered_people = list()
register = list()
light_people = list()
heavy_people = list()
control = 0


boolean = False

while boolean != True:
    print()
    print('---'*27)
    register.append(str(input('Enter a name: ')))
    
    print()  
    try:
        register.append(int(input(f"Enter the {register[0]}'s wight: ")))
    except:
        print('\n[Erro] re-register with the correct weight and name.')
        register.pop(-1)
        continue

    registered_people.append(register[:])
    register.clear()
    control += 1
    
    while True:
        print('---'*27)
        choise = str(input('\n--> Do you want to continue? [y-yes or n-not]')).lower()[0]

        if choise == 'n':
            boolean = True
            break
        elif choise == 'y':
            break
        else:
            print("[Alert!] Enter 'y' or 'n'!")

print('==='*27)
print(f'\n{control:-^9} people were registered!')

for c, weight in enumerate(registered_people):
    if c == 0:
        light_people.append(weight[:])
        heavy_people.append(weight[:])
    else:
        if light_people[0][1] == weight[1]:
            light_people.append[weight]
        elif light_people[0][1] > weight[1]:
            light_people.clear()
            light_people.append(weight[:])

        

if len(light_people) >= 1:
    print('\nThe lightest people are: ', end='')
    for c in light_people:
        print(f' {c}...', end='')
else:
    print('\nThere are no lighter people')

print()

if len(heavy_people) >= 1:
    print('\nThe heavy people are: ', end='')
    for c in heavy_people:
        print(f' {c}...', end='')
else:
    print('\nThere are no heavy people are: ', end='')
print()
print('==='*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Todo Sempre Seja Louvado. Amém.