print('==='*27)
print(' '*27,'Expressions')
print('==='*27)

pilha = list()

numbers = str(input('Enter a expression: --> '))

for c in numbers:

    if c == '(':
        pilha.append('(')

    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Your expression is correct!')
else:
    print('Your expression is not correct!')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.