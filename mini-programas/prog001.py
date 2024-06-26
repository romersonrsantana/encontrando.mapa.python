#bibliotecas
import emoji
from time import sleep
from datetime import date

#palete color
color = {'blue':'',
         'purple':'',
         'green':'',
         'yellow':'',
         'gray':'',
         'clean':''}

#title
print('\n','Calculando suas parcelas\n')

#dados p/ o programa
print('''Para prossegui com o programa, tenham em mãos: 
      1- O valor do veículo
      2- O valor de cada parcela''')

#dados de entrada do usuário:
amont = None
installment = None
cond = None

while True:
    amont = float(input('\nInforme o valor total da compra: ---> '))
    if amont >= 5000 and amont <= 300000:
        break
    else:
        print('\nOs valores deverão estar entre R$ 5.000,00 e R$ 300.000,00')
while True:
    installment = float(input('\nInforme a quantidade de parcelas que deseja: ---> '))
    cond = amont/installment    #parcelas informadas cliente
    porcentagem = amont*0.02    #2%
    if porcentagem <= cond:
        break
    else:
        print('\nO valor mínimo de cada parcela deverá ser de 2% do valor do veículo.\nOs dados informados correspondem a uma parcela de R$ {}, \nmenos de 2% do valor total de R${}. \nConsidere parcelas acima de R$ {}'.format(cond, amont, amont*0.02))
#Total de parcelas
quantidade_de_parcelas = (installment/12)
ano = date.today().year
print('\nConsiderando o total de parcelas informado de {} seu financiamento será quitado no ano de {}\n'.format(installment, ano + quantidade_de_parcelas))