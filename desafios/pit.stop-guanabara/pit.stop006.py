print('\n Primeira forma de solução \n')
#Algoritmo menos eficaz
for num in range(1, 51):
#Para verificar o número de repetições.
    print('.', end='')
#Condição para imprimir na tela:
    if num % 2 == 0:
        print(num, end=' ')
print('\nAcabou!!\n')

#Titulo
print('\n Solução Guanabara\n')
#Estrutura de Repetição
for num in range(2, 51, 2):
    #Para verificar quantas vezes o laço foi feito
    print('.', end='')
    #Laço de repetição
    print(num, end=' ')
print('Acabou!!')
