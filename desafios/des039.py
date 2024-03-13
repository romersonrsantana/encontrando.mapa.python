from datetime import date
#Paleta de Cores
colors = {'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'purple':'\033[1;35m',
          'blue':'\033[1;34m',
          'clean':'\033[m'}
#Titulo e introdução
print('\n','{}'.format(colors['green']),24*'===')
print('{}'.format(colors['clean']),' '*24,'{}Alistamento Militar Obrigatório!{}'.format(colors['yellow'],colors['clean']))
print(' ','{}'.format(colors['green']),'==='*24,'{}'.format(colors['clean']))
print('\nDigite uma opção válida para começar, que informe seu sexo:')               
print('[1]{}Sexo Feminino{}'.format(colors['purple'],colors['clean']))
print('[2]{}Sexo Masculino{}'.format(colors['blue'],colors['clean']))
opcao = int(input('---> '))
#Interação com o usuário
if opcao < 1 or opcao > 2:
    print('[Erro] Infome uma opção correta')
elif opcao == 1:
    print('\nPara as mulheres o alistamento não é obrigatório,\nO ingresso nas forças armadas poderá ser feito por meio de concursos.\n')

else:
    nasc = int(input('\nInforme seu ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
#Análisando os dados informados pelo usuário
    if nasc > ano or nasc <= 1924:
        print('\n[ERRO] Informe um ano válido.\n')
    elif idade <= 16:
        print('\nVocê é muito novo ainda não se preocupe com o alistamento militar, afinal tem apenas {} anos de idade,comece refletir a ideia quando estiver com quase 17 anos de idade.\n'.format(idade))
    elif idade == 18:
        print('\nSe você tem 18 anos procure o mais rápido possível quitar seus débitos com o exército, \npois o prazo para o alistamento começa no ano em que você irá completar 18 anos, \niniciando no dia 01 de janeiro indo até o dia 30 de junho.\n')
    elif idade == 17:
        print('\nFique atento pois no ano em que você irá completar 18 anos, já poderá realizar o alistamento no período do dia 01 de janeiro até o dia 30 de junho.\n')
    elif idade < 36:
        print('\nSério?? Se esse for mesmo seu ano de nascimento, acredito que tenha {} anos de idade. \nMelhor procurar um advogado porque você passou {} anos do périodo de alistamento.\n'.format(idade, idade-18))
    elif idade >= 36:
        print('\nSerio mesmo que você tem {} anos de idade??\nE que ainda assim não se alistou?\nAcho que você está me enrolando, tentando testar meu programa!!\n'.format(idade))
    else:
        print('\nCom {} anos de idade, sem ter feito o alistamento, \nvocê está com todos seus documentos bloqueados, \nprocure o Serviço Militar de seu Município e resolva sua pendências, \npois já passou {} anos do prazo para se alistar.\n'.format(idade,idade-18))

     

    


