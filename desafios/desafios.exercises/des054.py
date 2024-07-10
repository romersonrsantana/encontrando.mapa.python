from datetime import date
ano_atual = date.today().year

#palet_color
color = {'blue':'\033[1;34m',
         'purple':'\033[1;35m',
         'yellow':'\033[1;33m',
         'green':'\033[1;32m',
         'gray':'\033[1;37m',
         'alert':'\033[1;31m',
         'clean':'\033[m'}

print('\n',' '*18,'{}Identificando anos correspondentes a pessoas menores de idade.\n\n---> Os anos informados acima do ano atual de {}, serão desconsiderados.{}'.format(color['purple'],ano_atual,color['clean']))

#primeira fase, tentar identificar se o usuário irá colocar os quatro digitos do ano conforme solicitado.

#variáveis globais para controle.
SOMA = 0
MENOR_IDADE = 0
FORA_DO_PADRAO = 0
TODAS_IDADES = 0

for anos_nascimento in range (7):
#Estrutura de repetição, deverão ser informados 7x anos aleatórios.
    while True: 
        #estrutura de repetição para valores não iguais a 4 caracteres
        year = input('\n\nTell me some year, *with for digits: -->{} '.format(color['blue']))
        print('{}'.format(color['clean']))
        quantidade = len(year)

        if int(quantidade) == 4:          
            break
        else:
            print('\n',' '*18,'{}Valor inválido, digite um novo valor com quatro digitos!{}\n'.format(color['alert'], color['clean']))

    #Dados de saída. O laço SOMA indica na tela para o usuário quantas vezes o mesmo já digitou o valor solicitado e quantos ainda falta. 
    SOMA = SOMA + 1
    print('\n', ' '*9, '{}---> Valor'.format(color['green']),SOMA,'<---'.format(color['clean']))
    print('\n--> {}Falta informar mais {}{}{} valores para anos <--\n{}'.format(color['blue'],color['purple'],7 - SOMA,color['blue'],color['clean']))

    #Dados de Saída. Mensagem de erro caso o usuário tenha digitado letras.
    try:
        int(year)
    except ValueError:
        print('\n',' '*18,'{}[ALERT!] Você digitou outros caracteres ao invés de números!!!\n'.format(color['alert']),' '*18,'O valor informado não será considerado!{}\n'.format(color['clean']))
        continue
    convercao = int(year)
    
    #Depois de converter a string para int, será classificado os anos, ref.: acima ou abaixo de 18 anos.
    if ano_atual - convercao < 18 and ano_atual - convercao >= 0:
        MENOR_IDADE += 1
    elif ano_atual < convercao:
        FORA_DO_PADRAO += 1
    elif ano_atual - convercao > -1:
        TODAS_IDADES += 1

#Dados de saída para o usuário com os resultados.

print('\n\nEstamos em -->',ano_atual)
print('Dos anos informados:\n\n--> {}{}{} abaixo de --> 18 anos{}\n'.format(color['yellow'],MENOR_IDADE,color['gray'],color['clean']))
print('\n--> {}{}{} Fora da lógica{}. Ano de nascimento superior ao ano atual.\n'.format(color['yellow'],FORA_DO_PADRAO,color['gray'],color['clean']))
print('\n--> {}{}{} Válido(s) para {}Idades livres apartir de 18 anos{}.\n'.format(color['yellow'],TODAS_IDADES,color['clean'],color['green'],color['clean']))
