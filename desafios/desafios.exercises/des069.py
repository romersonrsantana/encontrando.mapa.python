print('\n',' '*27,'Customer registration\n\n',' '*27,'For customers aged 16 or over.\n') #cadastro do cliente 

control = age_eighteen = man = woman = 0
booleans = False

while booleans != True:

    control += 1
    
    while True:
        try:
            age = int(input(f'\nWhat is the age of the {control}st customer? ')) #Qual a idade do {controlador} cliente?
            if age >= 16:
                break
            else:
                print("\nThe age doesn't correspond to accepted criteria.\n") #a idade ñ corresponde aos critérios aceitos.
        except:
            print('\n[Alert] Enter numerical values!\n')

    if age >= 18:
        age_eighteen += 1

    while True:   
        
        gender = str(input(f'\nEnter the gender of the {control}st customer [F] for female or [M] for male:\n\n--> ')).lower().strip()[0] #Informe o gênero do {control} cliente [F] para feminino ou [M] para masculino.

        if gender == 'm' or gender == 'f':
            break
        else:
            print('\n[ERRO] Provide a correct option.\n') #Informe uma opção correta.
    
    if gender == 'm':
        man += 1
    
    if age < 20 and gender == 'f':
        woman += 1
    
    while True:
        choice = str(input('\nDo you want to continue customer registration? [y] yes or [n] not: \n\n --> ')).lower().strip()[0]
    
        if choice == 'n':
            booleans = True
            break
        elif choice == 'y':
            break
        else:
            print('\n[Alert] Incorrect option!\n')

print(f'\nThere are {age_eighteen} people aged 18 or over.\n')
print(f'\nThere are {man} men registered.\n')
print(f'\nThere are {woman} women under 20 years old.\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.