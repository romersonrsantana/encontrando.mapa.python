print('\n',' '*27,'Coletando dados\n')

soma_idade = 0

for dados in range(1, 5):
    nome = str(input('\n({}ª Pessoa) Informe seu nome: --> '.format(dados)))
    if dados == 1:
        nome1 = nome
    elif dados == 2:
        nome2 = nome
    elif dados == 3:
        nome3 = nome
    elif dados == 4:
        nome4 = nome
    
    idade = int(input('\n({}ª Pessoa) Informe sua idade: --> '.format(dados)))
    if dados == 1:
        idade1 = idade
    elif dados == 2:
        idade2 = idade
    elif dados == 3:
        idade3 = idade
    elif dados == 4:
        idade4 = idade

    sexo = int(input('''Digite 1 ou 2:
                     
                    1-Feminino
                      
                    2-Masculino
                     
                    ---> '''))
    if dados == 1:
        sexo1 = sexo
    elif dados == 2:
        sexo2 = sexo
    elif dados == 3:
        sexo3 = sexo
    elif dados == 4:
        sexo4 = sexo

    if sexo == 1 and idade < 20:
        soma_idade += 1
    
print(f'\nDados \nPessoa 1: {nome1}, {idade1}, {sexo1} \nPessoa 2 {nome2}, {idade2}, {sexo2},\nPessoa 3 {nome3}, {idade3}, {sexo3},\nPessoa 4 {nome4}, {idade4}, {sexo4} \n')

media_idade = (idade1 + idade2 + idade3 + idade4) / 4

if sexo1 == 2 or sexo2 == 2 or sexo3 == 2 or sexo4 == 2:
    if idade1 > idade2 and idade1 > idade3 and idade1 > idade4 and sexo1 == 2:
        print(f'\nO homem mais velho é {nome1}\n')
    elif idade2 > idade3 and idade2 > idade4 and idade2 > idade1 and sexo2 == 2:
        print(f'\nO homem mais velho é {nome2}\n')
    elif idade3 > idade1 and idade3 > idade2 and idade3 > idade4 and sexo3 == 2:
        print(f'\nO homem mais velho é {nome3}\n')
    elif idade4 > idade1 and idade4 > idade2 and idade4 > idade3 and sexo4 == 2:
        print(f'\nO homem mais velho é {nome4}.\n')

print(f'\nA média de idade dentro do programa foi de {media_idade} anos de idade.\n')

print(f'\nDentro do programa há {soma_idade} mulher(es) com menos de 20 anos.\n')
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.