print('==='*27)
print(' '*27,'Adapting values')
print('==='*27)

control = indice = 0
list= []

for c in range(0, 3):

    try:
        number = int(input('Enter a value: '))
    except:
        print('[ERRO] Enter an integer!')
        continue

    for c, v in enumerate(list):
        if number < list[c]:
            list.insert(c, number)
        else:
            list.append(number)

    control += 1

print(list)
