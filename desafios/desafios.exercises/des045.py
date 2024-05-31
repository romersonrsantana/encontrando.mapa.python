import random
from time import sleep
import emoji

num = random.randint(0, 2)
example_list = ["👊", "🤚", "✌"]
print('\n')
escolha = int(input('''Escolha um número: 
                    0 - Pedra 👊
                    1 - Papel 🤚
                    2 - Tesoura ✌
                    
                    ---> ''' ))
if escolha >= 0 and escolha < 3:
    print('Carregando...')
    sleep(3)
    if escolha == num:
        print('\nEmpatou!!\n')
    elif escolha < num != 1:
        print('\nVocê ganhou!!\n')
    elif escolha > num != 2:
        print('\nVocê ganhou!!\n')
    elif escolha > num != 1:
        print('\nVocê perdeu!!\n')
    elif escolha < num != 0:
        print('\nVocê perdeu!!\n')
    print('')
    print("Você escolheu ", example_list[escolha])
    print('')
    print("O computador escolheu ", example_list[num])
    print('')
else:
    print('\nTente uma opção válida!\n')
#Toda Honra e Toda Glória ao Deus de Israel, Ao Deus de Abraão, Isaac, Jacó e Moises. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.

