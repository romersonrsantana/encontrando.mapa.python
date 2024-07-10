from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for people in range(1, 8):
    year = int(input('\nEm que ano a {}ª pessoa nasceu? '.format(people)))
    idade = atual - year
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('\nSão: \n\n --> {} Maior idade. \n\n --> {} Menor idade.\n'.format(total_maior, total_menor))
