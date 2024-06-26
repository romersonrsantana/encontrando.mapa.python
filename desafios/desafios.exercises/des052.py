print('\n',' '*27,'Detectando números primos\n')
#dados usuário
number = int(input('\nInforme um número inteiro: --> '))
#condição
if number % 2 == 0:
    print('\nO número informado é PAR e COMPOSTO!')
elif number % 3 == 0:
    print('\nO número é IMPAR e COMPOSTO!')
elif number == 2:
    print('\nO número 2 é PAR e ao mesmo tempo PRIMO!\n')
elif number == 1:
    print('\nNão se classifica como número PRIMO.\n')
elif number == 0:
    print('\nNão é um número composto porque não atende a caracteristica de ser escrito como um produto dos números primos\n')
else:
    print('\nO número informado é PRIMO!')
