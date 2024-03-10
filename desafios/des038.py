colors = {'blue':'\033[1;4;34m',
          'purple':'\033[1;29;45m',
          'green':'\033[1;7;29;42m',
          'greentext':'\033[1;32m',
          'greentext1':'\033[1;4;32m',
          'yellow':'\033[1;7;33;42m',
          'yellowtext':'\033[1;33m',
          'yellowtext1':'\033[1;4;33m',
          'lightgreentext':'\033[1;36m',
          'lightgreentext1':'\033[1;4;36m',
          'clean':'\033[m'}

print('\n','==='*12, ' {} Comparador de números {}'.format(colors['purple'],colors['clean']), '=='*12, '\n')
print('{}Informe dois valores abaixo: {}\n'.format(colors['blue'],colors['clean']))

#dados usuário
n1 = float(input('{} First value:{} '.format(colors['green'],colors['clean'])))
n2 = float(input('\n{} Second value:{} '.format(colors['yellow'],colors['clean'])))

#comparando as informações

if n1 > n2:
    print('\n{} The first value entered is greater than the second value, {}that is {} > {}!!{}'.format(colors['greentext'],colors['greentext1'],n1,n2,colors['clean']))
elif n1 < n2:
    print('\n{} The second value enetered is greater than the first value, {}that is {} < {} !{}\n'.format(colors['yellowtext'],colors['yellowtext1'],n1,n2,colors['clean']))
else:
    print('\n{} The values are same!! {}{} == {} {}\n'.format(colors['lightgreentext'],colors['lightgreentext1'],n1,n2,colors['clean']))
