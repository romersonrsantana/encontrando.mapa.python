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
        
