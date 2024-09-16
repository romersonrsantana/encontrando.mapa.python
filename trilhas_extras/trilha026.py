print('==='*27)
print('Referências')
print()

spam = [0, 16, 28, 3, 2, 11]

cheese = spam

cheese[1] = 'hello'

print()
print(spam)
print()

spam[2] = 'world'
spam.insert(3, 16)
print(cheese)
print('==='*27)
print()

def eggs(some_parameter):
    some_parameter.append('hello')

spam = [1, 2, 3]
print(spam)
print()
eggs(spam)
print(spam)
print('==='*27)
print()
print('Cópiando listas\n')

import copy

spam = ['A', 'B', 'C', 'D']

cheese = copy.copy(spam)

cheese[1] = 16

print('\n',spam,'\n')

print('\n',cheese,'\n')


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés, Ao Seu Espiríto Santo e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.