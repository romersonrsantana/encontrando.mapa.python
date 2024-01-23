nome = str(input('\n\n Digite seu nome e sobrenome: ')).strip()
divisao = nome.split()
print('\n\n O nome digitado foi: {} \n\n Seu primeiro nome é: {} \n\n Seu último nome é: {}. \n\n Seu nome possui um total de {} caracteres.\n\n'.format(nome, divisao[0], divisao[len(divisao)-1], len(divisao[0])))