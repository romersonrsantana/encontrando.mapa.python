titulo = ' Car Rental '
print('\n\n Welcome to the simulator \n\n {:=^84} \n\n'.format(titulo))
custo = float(input('Rental days: '))
kms = float(input('\n Total kilometer: '))
print('\n\n The rent per day will be in the amount of R$60.00 and the cost per km R$0.15 \n\n R$60.00 x {} = {:.2f} \n\n R$0.15 x {} = {:.2f} \n\n Amount = R${:.2f} \n\n'.format(custo, (60.00*custo), kms, (0.15*kms), ((60.00*custo)+(0.15*kms))))