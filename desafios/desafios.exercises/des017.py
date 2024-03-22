import math

b = float(input('\n Digite o valor do cateto oposto que iremos chamar de b: '))
c = float(input('\n Digite o valor do cateto adjacente que iremos chamar de c: '))
hip = ((b ** 2 + c ** 2) ** (1/2))
print('\n Através dos valores digitados {} e {}, iremos calcular o valor da hipotenusa. \n\n A hipotenusa será: {:.2f} \n\n'.format(b, c, hip))

'''Resolução guanabara import math
hip = math.hypot(b, c)
'''