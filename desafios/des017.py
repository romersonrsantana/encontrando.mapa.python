import math

b = int(input('\n Digite o valor do cateto oposto que iremos chamar de b: '))
c = int(input('\n Digite o valor do cateto adjacente que iremos chamar de c: '))
print('\n Através dos valores digitados {} e {}, iremos calcular o valor da hipotenusa. A hipotenusa será {}'.format(b, c, (pow(b) + pow(c)))