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
print(' Processando...')
sleep(3)
if escolha == num:
    print('\n Empatou!! \n')
elif escolha < num != 1:
    print('\n Você ganhou!!\n')
elif escolha > num != 2:
    print('\n Você ganhou!!\n')
elif escolha > num != 1:
    print('\n Você perdeu!!\n')
elif escolha < num != 0:
    print('\n Você perdeu!!\n')
print('')
print("Você escolheu ", example_list[escolha])
print('')
print("O computador escolheu ", example_list[num])
print('')
#Toda Honra e Toda Glória ao Deus de Israel, Ao Deus de Abraão, Isaac, Jacó e Moises. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.

