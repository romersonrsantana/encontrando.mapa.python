#Paleta de cores
cores = {'limpa':'\033[m',
        'brancLil':'\033[1;29;45m',
        'lilas':'\033[1;35m',
        'vermelho':'\033[1;31m',
        'verde': '\033[1;32m',
        'azulbranc': '\033[1;7;44m'}

#titulo
print('\n',' '*12,'{}  Informações sobre o número  {}\n\n {} Siga as Orientações abaixo: {} \n'.format(cores['brancLil'],cores['limpa'],cores['lilas'],cores['limpa']))

#Entrada de informações pelo usuário
n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha um outro número: '))
if n1 == n2:
    print('\n \033[1;31m[ERRO] Os números escolhidos foram os mesmos!! \n Por favor, refaça suas escolhas!!\033[1;033m \n\n')
else:
    print('\n {} A soma dos dois números escolhidos são  {} + {} = {} {}\n\n '.format('\033[7;44m', n1,n2, (n1 + n2), cores['limpa']))
#Fazendo seu antecessor e sucessor
    print(20*'{}=-={}'.format(cores['verde'], cores['limpa']))
    print('Dos números relacionados: \n\n {}---- {} tem como antecessor {}  e como sucessor {} {}\n\n {}---- {} tem como antecessor {} e como sucessor {} {}\n\n'.format(cores['azulbranc'],n1,(n1-1),(n1+1),cores['limpa'],cores['azulbranc'],n2,(n2-1),(n2+1),cores['limpa']))
