import random
print('\nCorrida Maluca\n')

for corrida in range(6):
    num = random.randint(1,3)
    soma = 0
    somcomp = 0
    while True:
        jogador = int(input('Escolha um número de 1 a 3: ---> '))
        if jogador >= 1 and jogador <= 3:
            break
    if jogador == num:
        print('\nO computador escolheu {} e você escolheu {}\n'.format(num,jogador))
        print('\nPonto pra você!\n')
        s = 0
        for c in range(6):
            s = s + jogador
            print(s)
    else:
        print('\nO computador escolheu {} e você escolheu {}\n'.format(num,jogador))
        print('\nPonto para o computador!!\n')
        comp = 0
        for a in range(0,6):
            a = a + num
    
print()
print('Total de acertos jogador {}'.format(s))
print('Total de acertos computador {}\n'.format(a))
