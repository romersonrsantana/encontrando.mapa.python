print('\n',20*' ','Body Mass Index\n\n','Enter your details below\n\n')
weight = float(input('Tell us your weight: ---> '))

if weight <= 17 or weight >= 512:
    print('\nThe data provided is outside the established standard.\nRewrite the value.\n')
else:
    height = float(input('Tell us your heigth: ---> '))
    if height <= 0.70 or height > 4.50:
        print('\nThe date provided is outside the established standard.\nRewrite the value\n')
    else:
        BodyMass = weight/(height**2)
        if BodyMass < 18.5:
            print("\nYour body mass index {:.2f}\nYou're underweight".format(BodyMass))
        elif BodyMass >= 18.5 and BodyMass <= 25:
            print('')
