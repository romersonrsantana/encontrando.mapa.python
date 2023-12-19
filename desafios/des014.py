titulo = '  Celsus to Fahrenheit  '
print('\n\n {:=^90} \n\n Welcome to the temperature converter!!\n\n ' .format( titulo ))
degreesC = float(input('Enter the temperature in °C: '))
F = ((degreesC*9) + 160)/5
print('\n Converting {}°C to Fahrenheit we have {}°F \n\n' .format(degreesC, F))

