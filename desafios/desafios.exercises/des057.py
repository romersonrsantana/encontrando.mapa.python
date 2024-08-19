print('\n',27*' ','Coletando informações\n')
sexo = '0'
while sexo != 'M' and sexo != 'F':  
    sexo = str(input('\nInforme seu sexo, M para MASCULINO ou F para FEMININO --> ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('\nValor armazenado com sucesso!\n')
    else:
        print('\nOs dados informados não correspondem a solicitação de M ou F para o sexo correspondente!\n')
print('\nFim\n')