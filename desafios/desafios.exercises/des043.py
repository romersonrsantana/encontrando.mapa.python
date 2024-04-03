print('\n',20*' ','Body Mass Index\n\n','Enter your details below')
weight = float(input('Tell us your weight: ---> '))
if weight <= 17 or weight > 595:
    print('The data provided is outside the established standard.\nRewrite the value.\n')
else:
    height = float(input('Tell us your heigth'))
    if height <= 1.00 or height > 2.50:
        print('The date provided is outside the established,~LNLN standard. \n\n ')