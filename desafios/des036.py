#Color Palette
colors = {'blue':'\033[1;4;34m',
          'red':'\033[1;31m',
          'bluetext':'\033[7;1;44m',
          'bluemarc':'\033[1;34m',
          'clean':'\033[m'}
print('\n' , '   '*12 , '{} Financing Analysis {}'.format(colors['blue'], colors['clean']))
#user data (dados do usuário)
value = float(input('\n Inform the amount for financing: '))
if value < 40000.00 or value > 999000.00:
    print('\n {} The financing amount must be greater than U$40.000,00 and less than U$999.000,00 {} \n'.format(colors['red'], colors['clean']))
wage = float(input('\n Inform your monthly salary: '))
if wage < 1000.00:
    print('\n',21*'{}==='.format(colors['bluemarc']))
    print("\n{}{} The amount you receive is not ideal for financing.Please don't be discouraged! \n Start saving with what you have and your dream will be a reality!{}\n".format(colors['clean'],colors['bluetext'],colors['clean']))
    print('\n',21*'{}===','\n{}'.format(colors['bluemarc'],colors['clean']))
elif wage > 90000.00:
    print('\n',21*'{}===','\n{}'.format(colors['bluemarc'],colors['clean']))
    print('{} Sorry, but this financing is for people with a salary between US1.000,00 and US90.000,00. Leave your contact details and our consultants will contact you and indicate the ideal financing for you. Thanks!')
#Calculo para comprometimento da renda
    TRINTARENDA = wage*(30/100)
#Quantidade de parcelas
installmentsinyears = int(input('\n How many years, do you want to divide? '))
#calculo
debt = value/(installmentsinyears*12)   
if installmentsinyears > 31:
    print('{}\n The maximum number of installments is 30. {}\n'.format(colors['red'],colors['clean']))
elif installmentsinyears <= 1:
    print('{}\n It is not possible to finance with this number! {} \n'.format(colors['red'], colors['clean']))
else:
     print('\n O valor da sua dívida será {}\n'.format(debt))
print('Definindo se você terá direto ao financiamento {}'.format(TRINTARENDA))  
if TRINTARENDA < debt:
    print('\nThe amount for financing informed and the value of each installment exeed 30 of your salary :\n')
elif TRINTARENDA > debt:
    print('\n The period requested for financing was {} years.'.format(installmentsinyears))
    print('\n Financing will be contracted for a period of {} installments per month.'.format(installmentsinyears*12))
    print('\n The value of the installment will be U$ {}.\n'.format(debt))
