n1 = int(input('Escolha um número: '))
dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)

print('\n O número escolhido foi: {:=^ 28} , \n o doblo desse número é {:-> 28} , \n o triplo {:-> 28} .\n A raiz quadra corresponde {:-> 28}\n\n' .format(n1, dobro, triplo, raiz))