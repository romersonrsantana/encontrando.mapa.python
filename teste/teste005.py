import random
print('\nCorrida Maluca\n')
soma = 0
somcomp = 0

for corrida in range(6):
    num = random.randint(1,3)

    while True:
        jogador = int(input('Escolha um número de 1 a 3: ---> '))
        if jogador >= 1 and jogador <= 3:
            break
    if jogador == num:
        print('\nO computador escolheu {} e você escolheu {}\n'.format(num,jogador))
        print('\nPonto pra você!\n')
        soma = soma + 1
    else:
        print('\nO computador escolheu {} e você escolheu {}\n'.format(num,jogador))
        print('\nPonto para o computador!!\n')
        somcomp = somcomp + 1
    
print()
print('Total de acertos jogador {}'.format(soma))
print('Total de acertos computador {}\n'.format(somcomp))

if soma > somcomp:
    print('\n Você venceu!! \n')
elif soma == somcomp:
    print('\n Empate! \n')
else:
    print('\n Vitória do computador! \n')