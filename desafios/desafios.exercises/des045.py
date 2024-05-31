import random
import emoji

num = random.randint(0, 2)
example_list = ["👊", "🤚", "✌"]
escolha = int(input('''Escolha um número: 
                    0 - Pedra 👊
                    1 - Papel 🤚
                    2 - Tesoura ✌'''))

if escolha == num:
    print('Empatou')
elif escolha < num and escolha > num:
    print('Você ganhou!!')
elif escolha > num and escolha < num:
    print('Você perdeu!!')
elif escolha > num:
    print('Você perdeu!!')
elif escolha > num:
    print('Você ganhou!!')

print("O computador escolheu ", example_list[num])
