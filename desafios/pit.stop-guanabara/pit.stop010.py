print('\nResolução Guanabara')

maior = 0
menor = 0

for people in range(1, 6):
    peso = float(input('\nInforme o peso da {}ª pessoa: --> '.format(people)))

    if people == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso lido foi de {}KG'.format(maior))
print('\nO menor peso lido foi de {}KG\n'.format(menor))
