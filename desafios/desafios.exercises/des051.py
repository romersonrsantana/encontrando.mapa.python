from time import sleep
#Palete 

print('\n',' '*27,'Progressão Aritmética')

first = int(input('\nDigite um número inteiro que será o primeiro termo de uma P.A: ---> '))

reason = int(input('\nInforme um número inteiro que será a razão da P.A ---> '))
print()
sleep(0.7)
print('Calculando os 10 primeiros termos dessa P.A\n')
print()
sleep(1.6)
twentieth = first + reason*9

for c in range(first, twentieth + 1, reason):
    print(c,'-', end=' ')
print()
print('\nProgressão Aritmética concluida com sucesso!! \n')

