constante = 1/4.97

nome = input('\n\n Digite seu nome para iniciarmos: ')

real = float(input('\n\n Bem vindo a carteira digital {} ! Aqui você pode definir quanto de dólar deseja comprar. \n\n Insira seu valor de compra: ' .format(nome)))

print(' \n Com R$ {:.2f} reais você pode comprar U$ {:.2f} dolares! \n\n Obrigado por ter escolhido nossa carteira digital {} !! \n\n' .format(real, (real*constante), nome))