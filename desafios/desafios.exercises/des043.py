colors = {'blue':'\033[1;4;34m',
          'bluetext':'\033[1;34m',
          'purple':'\033[1;35m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'lightgreen':'\033[1;36m',
          'wrong':'\033[1;4;7;33;46m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}
#title
print('\n',20*' ','{}Body Mass Index{}\n\n'.format(colors['blue'],colors['clean']),'{}Enter your details below\n\n'.format(colors['purple']))
#peso
weight = float(input('\n{}Tell us your weight: --->{} '.format(colors['gray'],colors['green'])))
if weight <= 17 or weight >= 512:
    print('\n{}The data provided is outside the established standard.{}{}\n\nRewrite the value.{}\n'.format(colors['wrong'],colors['clean'],colors['lightgreen'],colors['clean']))
else:
    height = float(input('\n{}Tell us your heigth: --->{} '.format(colors['gray'],colors['green'])))
    if height <= 0.70 or height > 4.50:
        print('\n{}The date provided is outside the established standard.{}\n\n{}Rewrite the value{}\n'.format(colors['wrong'],colors['clean'],colors['lightgreen'],colors['clean']))
    else:
        BodyMass = weight/(height**2)
        if BodyMass < 18.5:
            print("\n{}Your body mass index {}{:.2f}\n\n{}You're underweight{}\n".format(colors['gray'],colors['yellow'],BodyMass,colors['wrong'],colors['clean']))
        elif BodyMass >= 18.5 and BodyMass < 25:
            print('\n{}Your body mass index is {}{:.2f}\n\n{}Your weight is{} ideal{} !!!{}\n'.format(colors['bluetext'],colors['purple'],BodyMass,colors['bluetext'],colors['purple'],colors['bluetext'],colors['clean']))
        elif BodyMass >= 25 and BodyMass < 31:
            print('{}\nYour body mass index is {}{:.2f}{} .You are {}overweight{} !!{}\n'.format(colors['green'],colors['yellow'],BodyMass,colors['green'],colors['yellow'],colors['green'],colors['clean']))
        elif BodyMass >= 31 and BodyMass < 41:
            print('\n{}Your body mass index is {}{:.2f}{} !! \n\nAttention {}obesity detected{} !!{}\n'.format(colors['lightgreen'],colors['yellow'],BodyMass,colors['lightgreen'],colors['yellow'],colors['lightgreen'],colors['clean']))
        elif BodyMass >= 41:
            print('\n{}Your body mass index is {}{:.2f}{} Attention!!{} Risk obesity{} !!{}\n'.format(colors['green'],colors['yellow'],BodyMass,colors['green'],colors['yellow'],colors['green'],colors['clean']))
