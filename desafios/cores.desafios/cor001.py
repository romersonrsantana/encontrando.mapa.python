from datetime import date
print('\033[1;34m=-=-'*9,'\033[1;31;45m Informe seus dados \033[m' ,'\033[1;34m=-=-\033[m'*8)
nome = str(input('Informe seu nome: '))
'''if len(nome) > 12:
    print('\n \033[1;31mReduza a quantidade de caracteres do seu nome \n')
else:'''
atual = date.today().year
idade = int(input('\n Qual sua idade?')) 
if idade < 0 or idade > 120:
    print('\n\n \033[1;31mHAHA!! Você deve está querendo testar meu progama. Tente uma idade válida \033[m\n\n')
else:
    mes = int(input('\n\n Informe seu mês de nascimento com até dois digitos: '))
    if mes < 1 or mes > 12:
        print('\n \033[1;31mSeu mês de aniversário não existe no calendário gregoriano\n')
    else:
        ano = int(input('\n Informe seu ano de nascimento com 4 digitos: '))
        if ano < 1904 or ano > atual:
            print('\n \033[1;31m[ERRO] Digite uma data válida \033[m \n\n')
        else:
            print('\n Nome: {} \n\n Idade: {} \n\n Mês: {} \n\n Ano: {} \n'.format(nome,idade,mes,ano))
