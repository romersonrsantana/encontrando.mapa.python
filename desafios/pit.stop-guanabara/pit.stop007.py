print()
print('Multiplos de 3')
print()
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c #O acumulador vai somando os valores
        contador = contador + 1 #O contador mostra a quantidade de números que ele acha a cada laço.
        print(' ',c, end=' ')

print('\n\n A soma de todos os vaores solicitados é {}\n'.format(soma))
print('O total de números multiplos de 3 encontrados nesse intervalo foram {}\n'.format(contador))
