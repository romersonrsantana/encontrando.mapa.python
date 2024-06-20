import random
import emoji
from ti1me import sleep

#color palete
color = {'blue':'\033[1;7;29;44m',
         'purple':'\033[1;29;45m',
         'yellow':'\033[1;33m',
         'green':'\033[1;32m',
         'gray':'\033[1;7;37m',
         'clean':'\033[m'}
#title
print('\n',' '*18,emoji.emojize("🏁 🏁 🏁 🏁 🏁 🏁"),'{} Corrida Maluca {}'.format(color['blue'],color['clean']),emoji.emojize("🏁 🏁 🏁 🏁 🏁 🏁"), '\n')
soma = 0
somcomp = 0

for corrida in range(5):
    num = random.randint(1,3)

    while True:
        sleep(1)
        print(' '*47,emoji.emojize("🔴"))
        sleep(1)
        print(' '*47,emoji.emojize("🟠"))
        sleep(1)
        print(' '*47,emoji.emojize("🟢"))
        sleep(1.8)
        print('\n')
        print(' '*47,emoji.emojize("🟢"))
        print(' '*47,emoji.emojize("🟢"))
        print(' '*47,emoji.emojize("🟢"))
        sleep(0.9)
        print()
        jogador = int(input('{}Escolha um número de 1 a 3: --->{} '.format(color['green'],color['yellow'])))
        if jogador >= 1 and jogador <= 3:
            break
    if jogador == num:
        sleep(0.9)
        print('\n{}O computador escolheu {}\n'.format(color['clean'],num))
        sleep(1)
        print('\n',' '*18,emoji.emojize("🚩 🚩 🚩 🚩 🚩 🚩"),'{}  Ponto pra você!  {}'.format(color['purple'], color['clean']),emoji.emojize("🚩 🚩 🚩 🚩 🚩 🚩"),'\n')
        sleep(0.5)
        print(' '*47,emoji.emojize("🚔 💨 💨 💨"))
        print()
        soma = soma + 1
    else:
        sleep(0.9)
        print('\n{}O computador escolheu {}\n'.format(color['clean'],num))
        sleep(0.8)
        print(' '*18,emoji.emojize("🏴‍☠️  🏴‍☠️  🏴‍☠️ "),'{} Ponto para o computador!! {}'.format(color['gray'],color['clean']),emoji.emojize("🏴‍☠️  🏴‍☠️  🏴‍☠️ "),'\n')
        sleep(0.5)
        print(' '*47, emoji.emojize("🚘 💨 💨 💨"))
        print()
        somcomp = somcomp + 1
    
print()
print('Total de acertos jogador {}'.format(soma))
print('Total de acertos computador {}\n'.format(somcomp))

if soma > somcomp:
    print(' '*27, emoji.emojize("🏆 🏆 🏆"), '{} Você venceu!! {}'.format(color['purple'],color['clean']) , emoji.emojize("🏆 🏆 🏆"), '\n')
    print('\n',' '*36, emoji.emojize("🏁 🏁 🏁 🚔 🏁 🏁 🏁"), '\n')
elif soma == somcomp:
    print('\n Empate! \n')
else:
    print(' '*27, emoji.emojize("🏆 🏆 🏆"),  '{} Vitória do computador! {}'.format(color['gray'],color['clean']), emoji.emojize("🏆 🏆 🏆"))
    print('\n',' '*36, emoji.emojize("🏁 🏁 🏁 🚘 🏁 🏁 🏁"), '\n')
