print('\n',' '*27, 'Estruturando uma P.A\n')

inicio = int(input('\nInforme um número inteiro para iniciar a P.A: \n\n--> '))

razao = int(input('\nInforme um número inteiro para ser a razão da P.A: \n\n--> '))

termo = inicio
controle = 9
contador = 0
new = 0

while contador < controle:
    contador += 1
    print('{}'.format(termo), end='')
    print(' >>> ' if contador < controle else ' Pausa. ', end='')
    termo += razao

    if contador == controle:
         new = int(input('\nMais quantos termos deseja?\n\n >>> '))
         print()
         controle += new

print('\nForam feitos uma P.A com {} termos!\n'.format(contador))

#É preciso confiar em Deus mesmo quando não entendemos nada. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.