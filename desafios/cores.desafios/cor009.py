#Paleta de cores
cores = {'azul':'\033[44m',
        'limpa':'\033[m'}
num = int(input('\n\n' + '\033[1;32;42m' + '- = '*6 + 'Para começarmos a tabuada' + ' - = '*6 + '\033[m' + '\n\nDigite um número inteiro: '))
print(6*'{}  '.format(cores['azul']))
print('{}{} x {} = {}'.format(cores['limpa'],num, 0, num*0))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, ))