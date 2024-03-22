nome = str(input('\n\n Para começar... Insira seu nome: ')).upper()
print('\n\n Seja bem vindo(a) ao nosso programa {}!!! \n\n Aqui você descobrirá se o número informado é: PAR ou IMPAR!\n\n'.format(nome))
numero = float(input('\n\n Informe um número inteiro: '))
if numero%2 != 0:
    print('\n\n O número informado é --- IMPAR --- não sendo uma divisão inteira.\n\n O resultado da divisão por dois tem como resto: {:.2f} \n\n'.format(numero%2))
else:
    print('\n\n O número escolhido é --- PAR ---- \n\n')
