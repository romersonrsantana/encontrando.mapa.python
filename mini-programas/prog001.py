#bibliotecas
import emoji
from time import sleep

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
installmentValue = None

while True:
    print('Informe o valor total da compra: ---> ')
    amont= input()
    if len(amont) >= 1:
         break

