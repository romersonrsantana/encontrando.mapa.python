from random import randint
from time import sleep
#criar uma variável usando ().
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
jogador = int(input('''Escolha um número:
                  [0] Pedra
                  [1] Papel
                  [2] Tesoura
                    ---> '''))
if jogador >= 0 and jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    print('')
    print('=-='*11)
    print('O computador escolheu {}'.format(itens[computador]))
    print('\nVocê escolheu {}'.format(itens[jogador]))
    print('=-='*11)
    #print('\nO computador escolheu {}\n'.format(itens[computador]))
    if computador == 0:
        if jogador == 0:
            print('\n Empatou!! \n')
        elif jogador == 1:
            print('\nVocê venceu!!\n')
        elif jogador == 2:
            print('\nVocê perdeu!!\n')

    elif computador == 1:
        if jogador == 0:
            print('\nVocê perdeu!!\n')
        elif jogador == 1:
            print('\nEmpatou!!\n')
        elif jogador == 2:
            print('\nVocê ganhou!!\n')
        
    elif computador == 2:
        if jogador == 0:
            print('\nVocê ganhou!!\n')
        elif jogador == 1:
            print('\nvocê perdeu!!\n')
        elif jogador == 2:
            print('\nEmpatou!!\n')
else:
    print('\nInforme uma opção correta\n')

