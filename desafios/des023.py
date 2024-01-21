n = int(input('\n Bem vindo ao analisador de números!! \n\n Digite um número com até quatro casas decimais: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('\n Caracteristica do número -- {} -- : \n\n Unidade: {} \n\n Dezena: {} \n\n Centena: {} \n\n Milhar: {} \n\n Obrigado!! \n\n'.format(n, u, d, c, m))