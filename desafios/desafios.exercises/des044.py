#colors palet
colors = {'blue':'\033[1;34m',
          'title-purple':'\033[1;45m',
          'purple':'\033[1;35m',
          'red':'\033[1;41m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'lightgreen':'\033[1;36m',
          'gray':'\033[1;37m',
          'clean':'\33[m'
          }
print('\n',12*'  ',' {} Payment methods {}\n'.format(colors['title-purple'],colors['clean']))
value = float(input('Inform the value of product: ---> U${} '.format(colors['green'])))
if value <= 0.4:
    print('\n{}   [ERRO] Enter a correct value!   {}\n'.format(colors['red'],colors['clean']))
elif value >= 0.5 and value <= 30:
    print('\n {}For the amount informed, the available payment\n method will be cash only.{} \n'.format(colors['blue'],colors['clean']))
else:
    print('{}'.format(colors['gray']))
    print('''\nChoice a payment methods
            1-Payment in cash or pix;
            2-On debit card;
            3-Up to 2x on credit card;
            4-3x or more on credit card;''')
    choice = int(input('\n Enter the number of the chosen option: -->{} '.format(colors['green'])))
    if choice < 1 or choice > 4:
        print('\n{}     [ERRO] Enter a valid number     {}\n'.format(colors['red'],colors['clean']))
    else:
        if choice == 1:
            print('\n {}With this payment method you will have a 20\%\ discount. \n\n The product it costs {} U$ {} {} \n\n In this form of payment, the discount will be {} U$ {} {}\n\n Amount {} U$ {} {}\n'.format(colors['clean'],colors['purple'],value,colors['clean'],colors['green'], (value*0.20),colors['clean'], colors['blue'], value-(value*0.2), colors['clean']))
        elif choice == 2:
            print('\n {}With this payment method you will have a 5\\%\\ discount. \n\n The product it costs {} U$ {}{}. \n\n In this form of payment, the discount will de {} U$ {}{}.\n\n Amount {} U$ {} {} \n'.format(colors['clean'],colors['purple'],value,colors['clean'],colors['green'],(value*0.05),colors['clean'],colors['blue'],value-(value*0.05),colors['clean']))
        elif choice == 3:
            installments = int(input('\n {}You want to divid the amount in 2x?\n\n {}1-yes{} \n\n {}2-No. Only 1x on credit card.{} \n\n --> {}'.format(colors['yellow'],colors['gray'],colors['clean'],colors['lightgreen'],colors['clean'],colors['gray'])))
            if installments < 1 or installments > 2:
                print('{}[ERRO] Write a valid value!{}'.format(colors['red'],colors['clean']))
            elif installments == 1:
                print('\n {}You will not receive discount with this payment method.\n\n The product it costs {}U$ {}{}. \n'.format(colors['blue'],colors['purple'],value,colors['clean']))
            elif installments == 2:
                print('\n You will not receive discount with this payment method.\n\n The product it costs {}U$ {}.\n\n {}In {} 2x installments {}you will pay a total of {}U$ {}{}.{}\n'.format(colors['green'],value,colors['gray'],colors['purple'],colors['gray'],colors['blue'],value/2,colors['gray'],colors['clean']))
        elif choice == 4:
            print('\n {}You can split it up to 10x with 20\\%\\ interest!\n'.format(colors['clean']))
            option = int(input('\nHow many time do you want to divide?{} '.format(colors['green'])))
            if option < 3 or option > 10:
                print('\n {}Reconsider your options, here you can split your purchases {}3x {}to {}10x {}times.{} \n'.format(colors['gray'],colors['yellow'],colors['gray'],colors['yellow'],colors['gray'],colors['clean']))
            else:
                print('\n {}Your purchases worth a total of {}U$ {}{}, will be divided into {}{} installments{}.\n Each installment will be worth {}U$ {} with interest{}.\n'.format(colors['clean'],colors['green'],value,colors['clean'],colors['purple'],option,colors['clean'],colors['blue'],(value+(value*0.2))/option,colors['clean']))
        
