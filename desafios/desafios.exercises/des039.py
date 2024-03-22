from datetime import date
#Paleta de Cores
colors = {'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'purple':'\033[1;35m',
          'purple2':'\033[1;4;35m',
          'blue':'\033[1;34m',
          'white':'\033[1;29m',
          'white2':'\033[1;4;30m',
          'red':'\033[1;30;41m',
          'red2':'\033[1;4;41m',
          'green':'\033[1;32m',
          'lightgreen':'\033[1;36m',
          'grey':'\033[1;37m',
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
    print('{} [Erro] Reinicie o programa e Infome uma opção correta {}\n\n'.format(colors['red'],colors['clean']))
elif opcao == 1:
    print('\n{}Para as mulheres o alistamento não é obrigatório,\nO ingresso nas forças armadas poderá ser feito por meio de concursos.{}\n'.format(colors['purple2'],colors['clean']))

else:
    nasc = int(input('\n{} Informe seu ano de nascimento:{} '.format(colors['yellow'],colors['clean'])))
    ano = date.today().year
    idade = ano - nasc
#Análisando os dados informados pelo usuário
    if nasc > ano or nasc <= 1924:
        print('\n{} [ERRO] Informe um ano válido. {}\n'.format(colors['red'],colors['clean']))
    elif idade <= 16:
        print('\n{}Você é muito novo não se preocupe com o alistamento militar.\nAfinal tem apenas {}{} anos de idade{}!\nComece refletir a ideia quando estiver com quase 17 anos de idade.{}\n'.format(colors['green'],colors['lightgreen'],idade,colors['green'],colors['clean']))
    elif idade == 18:
        print('\n{}Se você tem ou ainda vai completar 18 anos, neste ano de {}{}{}{} \nprocure o mais rápido possível o exército, \npois o prazo para o alistamento começa no ano em que você completa 18 anos,\n{}iniciando no dia 01 de janeiro indo até o dia 30 de junho.{}\n'.format(colors['white'],colors['blue'],ano,colors['clean'],colors['white'],colors['purple2'],colors['clean']))
    elif idade == 17:
        print('\n{}[ATENÇÃO]{} \n\n{}Fique atento pois no ano de {}{}{}{} em que você completa 18 anos, \njá poderá realizar o alistamento. \n\n{}No período do dia 01 de janeiro até o dia 30 de junho.{}\n'.format(colors['red'],colors['clean'],colors['green'],colors['lightgreen'],ano +1,colors['clean'],colors['green'],colors['red2'],colors['clean']))
    elif idade >= 19 and idade <= 20:
        print('\n {} [ALERTA!!] {} \n\n{}Sem o alistamento, você está em débito com seu Pais, com sua idade de {}{} anos{}{}, você deveria ter se alistado a pelo menos {}{} anos atrás{}{}!!{}\n\n'.format(colors['red'],colors['clean'],colors['lightgreen'],colors['white2'],idade,colors['clean'],colors['lightgreen'],colors['white2'],idade-18,colors['clean'],colors['lightgreen'],colors['clean']))
    elif idade > 25 and idade < 36:
        print('\n{}Sério?? Se esse for mesmo seu ano de nascimento, acredito que tenha {}{} anos de idade.{} \nMelhor procurar um advogado {}se ainda não se alistou{} \nporque você passou {}{} anos do périodo de alistamento.{}Isso deve ser até um crime!{}\n'.format(colors['green'],colors['yellow'],idade,colors['green'],colors['yellow'],colors['green'],colors['yellow'],idade-18,colors['green'],colors['clean']))
    elif idade >= 36:
        print('\n{}Serio mesmo que você tem {}{} anos de idade??{}\nE que ainda assim não se alistou?\n{}Você está me enrolando, tentando testar meu programa!!{}\n'.format(colors['grey'],colors['lightgreen'],idade,colors['grey'],colors['lightgreen'],colors['clean']))
    else:
        print('\n{}[DOCUMENTOS BLOQUEADOS]{}\n\n{}Com {}{} anos de idade{}, sem ter feito o alistamento, \n{}você está com todos seus documentos bloqueados{}, \nprocure o Serviço Militar de seu Município e resolva sua pendências, \npois já se passaram{} {} anos do prazo de alistamento{}.\n'.format(colors['red'],colors['clean'],colors['purple'],colors['blue'],idade,colors['purple'],colors['blue'],colors['purple'],colors['blue'],idade-18,colors['clean']))

     

    


