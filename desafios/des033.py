print('\n Relacionando números... \n')
n1 = float(input('\n\n Digite o primeiro número: '))
n2 = float(input('\n\n Digite o segundo número: '))
n3 = float(input('\n\n Digite o terceiro número: '))
print('\n\n Descobrindo o menor valor entre os três... \n\n')
if n1 < n2 and n1 < n3:
    print('\n\n O menor valor informado é: {}'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('\n\n O menor número é: {}'.format(n2))
    else:
        print('\n\n O menor número informado é: {} \n\n'.format(n3))

if n1 > n2 and n1 > n3:
    print('\n\n O maior valor informado é: {} \n\n'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('\n\n O maior valor informado é: {}\n\n'.format(n2))
    else:
        if n3 > n1 and n3 > n2:
            print('\n\n O maior valor informado é: {}\n\n'.format(n3))
