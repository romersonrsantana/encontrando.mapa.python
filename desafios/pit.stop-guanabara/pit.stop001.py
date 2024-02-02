from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('\n\n Parabéns!! Você venceu!!')
else:
    print('O computador venceu!! O número sorteado foi {} e o número que você escolheu foi {}'.format(computador, jogador))

