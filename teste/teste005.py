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
        x = 0
        for x in range(0, 9, 1):
            x = x + 1
            if x == 4:
                print("Você venceu")
                break
        print('\n {}'.format(x))
    else:
        print('\nO computador escolheu {} e você escolheu {}\n'.format(num,jogador))
        print('\nPonto para o computador!!\n')
        y = 0
        for y in range(0, 9):
            y = y + 1
            if y == 4:
                print("O computador venceu")
                break
        print('\n {}'.format(y))
    
print()
print('Total de acertos jogador {}'.format(x))
print('Total de acertos computador {}\n'.format(y))
