from datetime import date
print('\033[1;34m=-=-'*9,'\033[1;31;45m Informe seus dados \033[m' ,'\033[1;34m=-=-\033[m'*8)
nome = str(input('Informe seu nome: ')).upper()
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
        subtracao = atual - ano
        if subtracao > 130 or ano > atual:
            print('\n \033[1;31m[ERRO] Digite uma data válida \033[m \n\n')
        else:
            print('\n\033[1;32mNome:\033[m {}{} \n\n \033[1;32mIdade:\033[m {}{} anos \n\n \033[1;32mMês:\033[m {}{} \n\n\033[1;32mAno:\033[m {}{}{} \n'.format('\033[1;34m',nome,'\033[1;34m',idade,'\033[1;34m',mes,'\033[1;34m',ano,'\033[m'))
