print('==='*27)
print(' '*27,'Adapting values')
print('==='*27)

control = indice = 0
list= []

for c in range(0, 5):

    try:
        number = int(input('Enter a value: '))
    except:
        print('[ERRO] Enter an integer!')
        continue

    if control == 0:
        list.append(number)
    
    if number < d:
        list.insert(c, number)
    elif number > d:
        list.append(number)
    else:
        list.append(number)

    control += 1

    choise = str(input('Do you want to continue? [y-yes or N- not]')).lower()

    if choise == 'n':
        break

print(list)
