print('==='*27)
print(' '*27,'Adapting values')
print('==='*27)

control = indice = 0
list= []

def detail():
    print(' '*7,'List in ascending order --> ', end='')    
    for c in list:
        print(c, ' ... ' ,end='')
    print()

for c in range(0, 5):

    try:
        number = int(input('Enter a value: '))
    except:
        print('[ERRO] Enter an integer!')
        continue

    if control == 0:
        list.append(number)
    
    elif control == 1:
        if list[0] > number:
            list.insert(0,number)
        else:
            list.append(number)
    
    elif control == 2:
        if list[0] > number:
            list.insert(0, number)
        elif list[0] < number and number < list[1]:
            list.insert(1, number)
        else:
            list.append(number)
    
    elif control == 3:
        if list[0] > number:
            list.insert(0, number)
        elif list[0] <= number and number < list[1]:
            list.insert(1, number)
        elif number >= list[1] and number <= list[2]:
            list.insert(2, number)
        else:
            list.append(number)
    
    elif control == 4:
        if list[0] > number:
            list.insert(0, number)
        elif list[0] <= number and number < list[1]:
            list.insert(1, number)
        elif number >= list[1] and number <= list[2]:
            list.insert(2, number)
        elif number > list[2] and number <= list[3]:
            list.insert(3, number)
        else:
            list.append(number)

    control += 1
print()
print('---'*27)
detail()
print('---'*27)
print()

#Toda Honra e Toda Glória Ao Pai Celestial Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.