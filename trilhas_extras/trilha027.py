print('==='*27)
print(' '*27,'Code for commas')
print('==='*27)

spam = []
accountant = 0
value = 0

def control(control_list):
    for c in range(len(spam)):
        if c == 5:
            print(f' {spam[c]}.')
        elif c == 4:
            print(f'{spam[c]} and', end='')
        else:
            print(f'{spam[c]}, ', end='')


for c in range(0, 6):

    print(f'\nEnter 5 (five) items for the list, index {accountant:-^9} item --> ', end='')

    value = input().strip()

    if value == '':
        value = 'Value not informed.'
    
    spam = spam + [value]

    accountant += 1
    
print()
print('---'*27)
print('--> ', end='')
control(spam)
print('---'*27)
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés, Ao Seu Espírito Santo e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.