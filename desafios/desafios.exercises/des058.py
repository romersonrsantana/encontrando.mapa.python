import random

color_palet = {'blue':'\033[1;34m',
               'purple':'\033[1;35m',
               'yellow':'\033[1;33m',
               'green':'\033[1;32m',
               'alert':'\033[1;31m',
               'grey':'\033[1;37m',
               'clean':'\033[m'}

print('\n',' '*27,f'{color_palet["purple"]}Adivinhe o número{color_palet["clean"]}')

#sequencia para adivinhação
sequencia_numerica = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#algoritimo para escolha
escolhido_computador = random.choice(sequencia_numerica)

#inicio para entrar no laço while
escolhido_jogador = 11

#contador para controle de acertos
soma = 0

while escolhido_computador != escolhido_jogador:
    try:
        escolhido_jogador = int(input(f'\nEscolha um número entre 0 e 10: -->{color_palet["blue"]} '))
        print(f'{color_palet["clean"]}')
    except:
        print('\n',' '*18,'{}[Alert!]{} O valor digitado não é válido!\n\n'.format(color_palet['alert'],color_palet['grey']),' '*18,'  Tente valores entre 0 e 10!!\n{}'.format(color_palet['clean']))
        continue
    if escolhido_jogador < 0 or escolhido_jogador > 10:
        print('\n',' '*18,'{}[Alert!]{} Escolha um número válido entre 0 e 10.{}'.format(color_palet['alert'],color_palet['grey'],color_palet['clean']))
    elif escolhido_jogador == escolhido_computador:
        print('\n',' '*27,'{}Parabéns você acertou!{}'.format(color_palet['yellow'],color_palet['clean']))   
    
    soma += 1

print(' '*27,f'\n{color_palet["grey"]}Foram necessárias {color_palet["green"]}{soma}{color_palet["grey"]} tentativas!!{color_palet["clean"]}\n')