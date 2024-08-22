print('\n',' '*27,'Fatorial\n')

controle = False

while not controle:
    try:
        numero = int(input('Informe um número: --> '))
        if numero >= 0:
            controle = True
    except:
        print('\n[Alert] Informe um valor aceitavel para iniciar!\n')
        continue

print()
print('O fatorial de {}! é: \n\n>>> '.format(numero), end='')
total = 1

for c in range(numero, 0 , -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    total *= c
print(total,'\n')

#Toda Honra e Toda Glória Ao Deus de Betel. Toda Honra e Toda Glória Ao Espirito Santo. Toda Honra e Toda Glória A Jesus. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.