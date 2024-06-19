print('Somando números inteiros, pares')
s = 0
print('Digite seis valores e iremos somar apenas os pares:')
print()
for c in range(1, 7):
    choice = int(input('\nvalor {} : ---> ' .format(c)))
    if choice % 2 == 0:
        s = s + choice
if choice % 2 == 0:
    print(choice)
print('A soma dos números pares são {}'.format(s))
print()


