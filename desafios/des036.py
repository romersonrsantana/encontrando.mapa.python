#Color Palette
colors = {'blue':'\033[1;4;34m',
          'red':'\033[1;31m',
          'clean':'\033[m'}
print('\n' , '   '*12 , '{} Financing Analysis {}'.format(colors['blue'], colors['clean']))
value = float(input('\n Inform the amount for financing: '))
if value < 40000.00 or value > 999000.00:
    print('\n {} The financing amount must be greater than U$40.000,00 and less than U$999.000,00 {} \n'.format(colors['red'], colors['clean']))
wage = float(input('\n Inform your monthly salary: '))
