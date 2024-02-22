#Paleta de cores
cores = {'azul':'\033[44m',
         'lilasbranc':'\033[1;29;45m',
         'brancpreto':'\033[7;1;29m',
        'limpa':'\033[m'}
num = int(input('\n\n' + '\033[1;32;42m' + '- = '*6 + 'Para começarmos a tabuada ' + ' - = '*6 + '\033[m' + '\n\nDigite um número inteiro de 0 a 10: '))
if num < 0 or num > 10:
    print('\n\033[7;1;29m[Erro] Nesse programa só será possivel aprender a tabuada de multiplicação entre 0 e 10!!!\nPor favor, refaça sua escolha...',56*' ','\033[m\n')
          #.format(cores['brancpreto'],cores['limpa']))
else:
    print('\n')
    print(4*'{}     '.format(cores['azul']))
    print('{}{}{:3} x {:4} = {:5}  {}'.format(cores['limpa'],cores['lilasbranc'],num, 0, num*0,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 1, num*1,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 2, num*2,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 3, num*3,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 4, num*4,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 5, num*5,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 6, num*6,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 7, num*7,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 8, num*8,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 9,  num*9,cores['limpa']))
    print('{}{:3} x {:4} = {:5}  {}'.format(cores['lilasbranc'],num, 10, num*10,cores['limpa']))
    print(4*'{}     '.format(cores['azul']))
    print('{}'.format(cores['limpa']))
