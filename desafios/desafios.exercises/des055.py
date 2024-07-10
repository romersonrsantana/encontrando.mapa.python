#palet color
color = {'blue':'\033[1;34m',
         'purple':'\033[1;35m',
         'yellow':'\033[1;33m',
         'green':'\033[1;32m',
         'gray':'\033[1;37m',
         'alert':'\033[1;31m',
         'clean':'\033[m'}
#titulo
print('\n',' '*27,'{}Identificando pesos{}\n'.format(color['purple'], color['clean']))

#variável para armazenar valores do laço.
people = []

#estrutura para controle
for kg in range (1,6):

    #laço que determina os parâmetros dos valores aceitaveis
    while True:

        #evita que o programa trave, considera erro de str para float
        try:
            peso = (float(input('\nInforme o {}{}ª{} peso humano: -->{} '.format(color['blue'],kg,color['clean'],color['blue']))))
            print(f'{color["clean"]}')    
        except ValueError:
            print('\n',' '*9,f'{color["alert"]}[ERRO]{color["gray"]} Você digitou outros tipos de caracteres que não correspondem a números!{color["alert"]}\n',' '*9, f'[ALERT] O valor passado não será considerado!!{color["clean"]}\n')
            continue
        #parâmetros
        if peso > 1 and peso <= 595:
            break
        elif peso > 595:
            print(f'\n{color["alert"]}[ERRO]{color["gray"]} Informe um valor válido, o maior peso que se te registro \né do Mexicano Juan Pedro Franco com 595KG.{color["clean"]}')
        elif peso < 0.45:
            print(f'\n{color["alert"]}[ERRO]{color["gray"]} O valor minimo considerado é de recém nascidos com até 450G{color["clean"]}\n')

    #adiciona os valores no vetor a cada iteração.
    people.append(peso)

#definição do maior e menor valor inserido.
maior_peso = max(people)
menor_peso = min(people)

#resultado na tela
print(f'\n\n{color["gray"]}Os pesos são: --> {color["green"]}{people}{color["clean"]}\n\n{color["green"]}---> O maior peso será: {color["yellow"]}{maior_peso}{color["green"]}\n\n---> O menor peso será: {color["yellow"]}{menor_peso}{color["clean"]}\n')
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.