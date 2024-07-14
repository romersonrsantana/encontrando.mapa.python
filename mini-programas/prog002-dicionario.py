import re
#busca_com_espaco = re.compile("[\s]")
#busca = 0 --> Entender REGEX - Problema: --> Aceitar caracteres com espaço.

color = {'blue':'\033[1;34m', 
         'purple':'\033[1;35m',
         'gray':'\033[1;37m',
         'clean':'\033[m'}

print('\n',' '*27,'{}Informe os dados para cadastro{}\n'.format(color['purple'], color['clean']))

mulhere_menos_20anos = 0
nome_mais_velho = 0
maior_idade = 0
teste_string_vazia = ('aeiou')

for dados in range(1, 5):

    while True:

        nome = str(input('\nInforme o nome do {}º cliente: -->{} '.format(dados, color['blue']))).strip().title()
        print(f'{color["clean"]}')
        
        #A string foi fatiada e em seguida será feito um teste de verificação para saber se foi digitado apenas letras.

        teste = nome[:2]
        test = teste.isalpha()

        if test == True:
            break
        else:
            print(f'\n{color["gray"]}Insira um nome válido{color["clean"]}\n')
    
    while True:
        try:
            idade = int(input('\nQual a idade do {}º cliente:{} --> '.format(dados,color['blue'])))
            print(f'{color["clean"]}')
            if idade >= 18 and idade <= 97:
                break
            else:
                print('\nInforme uma idade válida entre 18 e 97 anos\n')
        except ValueError:
            print(f'\nVocê não digitou caracteres númericos.\n\n {color["gray"]}[Alert!]{color["clean"]} Verifique o valor novamente.\n')
            continue
    
    while True:
        sexo = str(input(f'\nDigite o sexo do {dados}º cliente, se é masculino ou feminino: --->{color["blue"]} ')).upper().strip()
        print(f'{color["clean"]}')
        if sexo == 'MASCULINO':
            break
        elif sexo == 'FEMININO':
            break
        else:
            print(f'\n{color["gray"]}[ALERT!]{color["clean"]} Você não informou corretamente o sexo do {dados}º cliente.\n')

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

print(f'\n{color["purple"]}Dados armazenados com sucesso!{color["clean"]}\n\n--> {dados_cliente1} \n--> {dados_cliente2} \n--> {dados_cliente3}\n--> {dados_cliente4}\n')

print(f'\nO homem mais velho:\n\n --> {color["blue"]}{nome_mais_velho}{color["clean"]} com {maior_idade} anos de idade.\n')

print(f'\nDos dados armazenados de mulheres com menos de 20 anos de idade:\n\n --> {color["purple"]}{mulhere_menos_20anos} com menos de 20 anos{color["clean"]}.\n')
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.