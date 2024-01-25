print('\n\n Bem vindo ao Programa Escolar!! \n\n Aqui vamos calcular sua média \n\n Considerando a escala de 0 a 10!!')
n1 = int(input('\n\n Digite sua nota do primeiro bimestre: '))
n2 = int(input('\n\n Digite sua nota do segundo bimestre: '))
media = (n1+n2)/2
print('\n\n Sua média foi de {} !'.format(media))
if media >= 6:
    print('\n\n Parabéns você atingiu a média!!\n\n')
else:
    print('\n\n Sua média foi ruim!! estude mais!!\n\n')