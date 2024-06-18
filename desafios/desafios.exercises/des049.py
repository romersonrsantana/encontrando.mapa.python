import emoji
print('\nTabuada com estrutura de repetição\n')

while True:
    number = int(input('Insira um número inteiro entre 0 e 10: '))
    if number >= 0 and number < 11:  
        break
print()
while True:
    print(emoji.emojize("🟦🟦🟦🟦"*9))
    print()
    choice = int(input('''Escolha uma opção de tabuada:
      1 = Tabuada de Subtração
      2 = Tabuada de Adição
      3 = Tabuada de Multiplicação
      4 = Tabuada de Divisão
        ---> '''))
    if choice > 0 and choice < 5:
        print()
        print(emoji.emojize("🟦🟦🟦🟦"*9))
        break
print()
if choice == 1:
    print(emoji.emojize("🟧🟧🟧🟧"*9))
    if number == 0:  
        for c in range(0, 11):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))       
    elif number == 1:
        for c in range(1, 12):
            print(' '*27, '{} - {} = {}'.format(c, number, (c - number)))
    elif number == 2:
        for c in range(2, 13):
            print(' '*27,)
        
print()
        print(emoji.emojize("🟧🟧🟧🟧*9"))

print(emoji.emojize("🟪🟪🟪🟪"*9))
print()

for c in range(0, 11):
    print(' '*27,'{} x {} = {}'.format(number, c, number*c))

print()
print(emoji.emojize("🟪🟪🟪🟪"*9))
    
    
   
