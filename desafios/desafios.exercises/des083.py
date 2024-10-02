print('==='*27)
print('Numerical expressions')
print('==='*27)

list = []
control = 0
control_2 = 0

numbers = str(input('Write a numerical expressions with parenteses:\n\n--> '))

list.append(numbers)

for c in numbers:
    if c == '(':
        control += 1
    if c == ')':
        control_2 += 1

print()
if control == control_2:
    print('For each open parenthesis a corresponding closed parenthesis was found.')
else:
    print('[Alert] The parenthesis was not closed correctly.')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.