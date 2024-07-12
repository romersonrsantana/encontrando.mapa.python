print('\nInforme os dados para cadastro\n')

mulhere_menos_20anos = 0
nome_mais_velho = 0
maior_idade = 0


for dados in range(1, 5):

    nome = str(input('\nInforme o nome do {}º cliente: --> '.format(dados)))

    while True:
        try:
            idade = int(input('\nQual a idade do {}º cliente: --> '.format(dados)))
            if idade >= 18 and idade <= 97:
                break
            else:
                print('\nInforme uma idade válida entre 18 e 97 anos\n')
        except ValueError:
            print('\nVocê não digitou caracteres númericos.\n\n [Alert!] Verifique o valor novamente.\n')
            continue
    
    while True:
        sexo = str(input(f'\nDigite o sexo do {dados}º cliente, se é masculino ou feminino: ---> ')).upper().strip()
        print()
        if sexo == 'MASCULINO':
            break
        elif sexo == 'FEMININO':
            break
        else:
            print(f'\n[ALERT!] Você não informou corretamente o sexo do {dados}º cliente.\n')

    if dados == 1:
        dados_cliente1 = {'cliente1': nome,'idade': idade, 'sexo': sexo}
    elif dados == 2:
        dados_cliente2 = {'cliente2': nome, 'idade': idade, 'sexo': sexo}
    elif dados == 3:
        dados_cliente3 = {'cliente3': nome, 'idade': idade, 'sexo': sexo}
    elif dados == 4:
        dados_cliente4 = {'cliente4': nome, 'idade': idade, 'sexo': sexo}
    
    if dados == 1 and sexo == 'MASCULINO':
        maior_idade = idade
        nome_mais_velho = nome
    else: 
        if idade == maior_idade and sexo == 'MASCULINO':
            nome_mais_velho = 'Mais de um homem possui a mesma idade'
            maior_idade = idade
        elif idade > maior_idade and sexo == 'MASCULINO':
            maior_idade = idade
            nome_mais_velho = nome
    
    if sexo == 'FEMININO'and idade < 20:
        mulhere_menos_20anos += 1

print(f'\nDados armazenados com sucesso!\n\n--> {dados_cliente1} \n--> {dados_cliente2} \n--> {dados_cliente3}\n--> {dados_cliente4}\n')

print(f'\nO homem mais velho:\n --> {nome_mais_velho} com {maior_idade} anos de idade.\n')

print(f'\nDos dados armazenados de mulheres com menos de 20 anos de idade:\n --> {mulhere_menos_20anos} com menos de 20 anos.\n')
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.