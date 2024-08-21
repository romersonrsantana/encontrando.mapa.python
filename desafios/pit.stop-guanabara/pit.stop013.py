print('\n',' '*27,'Fatorial\n')

numero = int(input('\nInforme um número para iniciar: --> '))

controle = numero
fatorial = 1

print('\nO fatorial de {}! será: >>> '.format(numero), end='')

while controle > 0:
    print(' {} '.format(controle), end='')
    print(' x ' if controle > 1 else ' = ', end='' )
    
    fatorial *= controle
    controle -= 1
print(f'{fatorial}\n')

#Sagrado Coração de Jesus eu confio em Vós. Sagrado Coração de Jesus eu espero em Ti. Amém.