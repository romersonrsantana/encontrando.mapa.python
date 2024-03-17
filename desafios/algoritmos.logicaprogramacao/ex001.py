#colors palette
colors ={ 'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'red':'\033[1;31m',
          'clean':'\033[m',
         }

print('\n',' '*20,'{}Analisador de moedas{}'.format(colors['blue'],colors['clean']))
#O peso das moedas foram dividos(Total de moedas 5),  e o resultado de cada moeda será colocada dentro em uma variável,

#calculo
print('\nConsiderando os valores que estão no computador')
PM1 = 5
PM2 = 5
PM3 = 5
PM4 = 5
PM5 = 5

soma1 = PM1 + PM2
soma2 = PM3 + PM4

if soma1 == soma2 and PM1 != PM5:
    print('\n{}A Moeda falsa está na variavel PM5{}\n'.format(colors['red'],colors['clean']))
elif PM1 != PM2:
    print('\nA moeda falsa está em PM1 ou PM2\n')
    if PM1 != PM5:
        print('\n{}PM1 é a moeda falsa!{}\n'.format(colors['red'],colors['clean']))
    else:
        print('\n{}PM2 é a moeda falsa!{}\n'.format(colors['red'],colors['clean']))
elif PM3 != PM4:
    print('\nA moeda falsa está entre PM3  e PM4!\n')
    if PM3 != PM5:
        print('\n{}A moeda falsa é PM3!{}\n'.format(colors['red'],colors['clean']))
    else:
        print('\n{}A moeda falsa é PM4!!{}\n'.format(colors['red'],colors['clean']))
else:
    print('\n{}Todas as moedas são verdadeiras!!{}\n'.format(colors['purple'],colors['clean']))

