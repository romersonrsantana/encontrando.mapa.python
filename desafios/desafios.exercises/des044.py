print('\n',12*'  ',' Payment methods\n')
value = float(input('Inform the value of product: ---> U$ '))
if value <= 0.4:
    print('\n[ERRO] Enter a correct value!\n')
elif value >= 0.5 and value <= 30:
    print('\nFor the amount informed, the available payment\n method will be cash only.')
else:
    print('''\nChoice a payment methods
            1-Payment in cash or pix;
            2-On debit card;
            3-Up to 2x on credit card;
            4-3x or more on credit card;''')
    choice = int(input('\n Enter the number of the chosen option: --> '))
    if choice < 1 or choice > 4:
        print('\n [ERRO] Enter a valid number \n')
    else:
        if choice == 1:
            print('\n With this payment method you will have a 20\%\ discount. \n\n The product it costs U$ {} \n\n In this form of payment, the discount will be U$ {} \n\n Amount {}'.format(value, (value*0.20), value-(value*0.2)))
        elif choice == 2:
            print('\n With this payment method you will have a 5\\%\\ discount. \n\n The product it costs U$ {}. \n\n In this form of payment, the discount will de U$ {}.\n\n Amount {}'.format(value, (value*0.5), value-(value*0.5)))
        elif choice == 3:
            installments = int(input('\n You want to divid the amount in 2x? \n\n 1-yes \n\n 2-no. Only 1x on credit card.'))
            if installments < 1 or installments > 2:
                print('[ERRO] Write a valid value!')
            elif installments == 1:
                print('\nYou will not receive discount with this payment method.\n\n The product it costs U$ {}. \n')
            elif installments == 2:
                print('\nYou will not receive discount with this payment method.\n\n The product it costs U$ {}.\n\n In 2x installments you will pay a total of {}\n'.format(value,value/2))
        elif choice == 4:
            print('You can split it up to 10x with 20\\%\\ interest!\n')
            option = int(input('\nHow many time do you want to divide? '))
            if option < 3 or option > 10:
                print('\n Reconsider your options, here you can split your purchases 3x to 10x times \n')
            else:
                print('\n Your purchases worth a total of U$ {}, will be divided into {} installments.\n Each installment will be worth {} with interest.\n'.format(value,option,(value+(value*0.2))/option))
        
