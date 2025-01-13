import random

def layout(caractere, msg):
    print(f'{caractere}'* 36)
    print(' '*36, f'{msg}')
    print(f'{caractere}'* 36)


def number_draw():
    return random.randint(1, 126)

def even_numbers():
    soma = 0
    for c, v in enumerate(numbers):
        if v % 2 == 0:
            soma += v
    print(f'            The sum of the even numbers is {soma}.')
        

layout('===', 'Number Separator')

numbers = list()
control = 0

while True:

    layout('~~~', f'        Total numbers drawn: {control + 1}.')

    num = number_draw()

    if control == 0:
        numbers.append(num)
    else:
        if num not in numbers:
            numbers.append(num)
    
    choise = str(input('>>> Do you want to continue? [y- yes or n-not] '))[0].lower()

    if choise == 'n':
        break
    elif choise == 'y':
        control += 1
        continue
    else:
        layout('---', "Report 'y' or 'n'! ")
    
layout('===', 'Result')
print(f'            The numbers draw are: {numbers}.')
even_numbers()
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Único Filho Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.