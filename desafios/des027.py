nome = str(input('\n\n Digite seu nome e sobrenome: '))
divisao = nome.split()
print('\n\n O nome digitado foi: {} \n\n Seu primeiro nome é: {} \n\n Seu sobrenome: {}. \n\n Seu nome possui um total de {} caracteres.\n\n'.format(nome, divisao[0], divisao[1:], len(divisao)))