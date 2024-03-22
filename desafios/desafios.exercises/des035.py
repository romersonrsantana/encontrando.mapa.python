print('\n\n Condição de existência: --- triangulo ---- \n\n informe o tamanho de 3 retas e descubra se elas podem formar um triângulo...\n\n')
reta1 = float(input('Informe o tamanho da reta 01: '))
reta2 = float(input('\n\n Informe o tamanho da reta2: '))
reta3 = float(input('\n\n Informe o tamanho da reta 03: '))
if (reta2 + reta1) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('\n\n Com essas retas é possivel formar um triangulo.\n\n')
else:
    print('\n\n Não é possivel formar um triângulo!!\n\n')
