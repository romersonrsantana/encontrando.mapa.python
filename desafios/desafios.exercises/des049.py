import emoji
#color palete
color = {'blue':'\033[1;35;44m',
         'purple':'\033[1;35m',
         'clean':'\033[m'}

print('\n',' '*27,'{} Tabuada com estrutura de repetição {}\n'.format(color['blue'],color['clean']))

while True:
    number = int(input('Insira um número inteiro entre 0 e 10:{} '.format(color['purple'])))
    if number >= 0 and number < 11:  
        break
print('{}'.format(color['clean']))
print()
while True:
    print(emoji.emojize("🟦🟦🟦🟦"*9))
    print()
    choice = int(input('''Escolha uma opção de tabuada:
      1 = Tabuada de Subtração
      2 = Tabuada de Adição
      3 = Tabuada de Multiplicação
      4 = Tabuada de Divisão
        --->{} '''.format(color['purple'])))
    if choice > 0 and choice < 5:
        print()
        print(emoji.emojize("🟦🟦🟦🟦"*9))
        break
print('{}'.format(color['clean']))

if choice == 1:
    print(emoji.emojize("🟧🟧🟧🟧"*9))
    print()
    if number == 0:  
        for c in range(0, 11):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))       
    elif number == 1:
        for c in range(1, 12):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 2:
        for c in range(2, 13):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 3:
        for c in range(3, 14):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 4:
        for c in range(4, 15):
            print(' '*27,'{} - {} = {}'.format(c, number, (c - number)))
    elif number == 5:
        for c in range(5, 16):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 6:
        for c in range(6, 17):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 7:
        for c in range(7, 18):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 8:
        for c in range(8, 19):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 9:
        for c in range(9,20):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 10:
        for c in range(10, 21):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    print()
    print(emoji.emojize("🟧🟧🟧🟧"*9))
    print()
#Adição
elif choice == 2:
    print(emoji.emojize("🟨🟨🟨🟨"*9))
    print()
    for c in range(1, 11):
        print(' '*27, '{} + {} = {}'.format(number, c,  (number + c)))
    print()
    print(emoji.emojize("🟨🟨🟨🟨"*9))
    print()
#Multiplicação
elif choice == 3:
    print(emoji.emojize("🟩🟩🟩🟩"*9))
    print()
    for c in range(0, 11):
        print(' '*27, '{} x {} = {}'.format(number, c,  (number*c)))
    print()
    print(emoji.emojize("🟩🟩🟩🟩"*9))
    print()
#Divisão
elif choice == 4:
    print(emoji.emojize("🟪🟪🟪🟪"*9))
    print()
    if number == 1:
        for c in range(1, 11):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 2:
        for c in range(2, 22, 2):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 3:
        for c in range(3, 33, 3):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 4:
        for c in range(4, 44, 4):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 5:
        for c in range(5, 55, 5):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 6:
        for c in range(6, 66, 6):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 7:
        for c in range(7, 77, 7):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 8:
        for c in range(8, 88, 8):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 9:
        for c in range(9, 99, 9):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    elif number == 10:
        for c in range(10, 110, 10):
            print(' '*27, '{} / {} = {}'.format(c, number, (c/number)))
    else:
        print(' Não existe divisão por zero, refaça o programa e tente novamente!')
print()   
print(emoji.emojize("🟪🟪🟪🟪"*9))
print()
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.