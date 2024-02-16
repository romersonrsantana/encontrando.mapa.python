#Paleta de cores
cores = {'limpa':'\033[m',
        'brancLil':'\033[1;29;45m',
        'lilas':'\033[1;35m'}

#titulo
print('\n',' '*12,'{}  Informações sobre o número  {}\n\n {} Siga as Orientações abaixo: {} \n'.format(cores['brancLil'],cores['limpa'],cores['lilas'],cores['limpa']))

#Entrada de informações pelo usuário
n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha um outro número: '))
if n1 == n2:
    print('\n [ERRO] Os números escolhidos foram os mesmos!! \n Por favor, refaça suas escolhas!! \n\n')
