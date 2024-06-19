print('Somando números inteiros, pares')
s = 0
print('Digite seis valores e iremos somar apenas os pares:')
print()
for c in range(1, 7):
    choice = int(input('valor {} : --->' .format(c)))
    if choice % 2 == 0:
        s = s + choice

print()
print('{}', end=' '.format(choice))
print('A soma dos números pares são {}'.format(s))
print()


