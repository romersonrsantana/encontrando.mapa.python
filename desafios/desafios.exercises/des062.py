colors = {'Purple':'\033[1;35m',
          'Blue':'\033[1;34m',
          'Yellow':'\033[1;33m',
          'Green':'\033[1;32m',
          'Alert':'\033[1;31m',
          'Gray':'\033[1;37m',
          'Clean':'\033[m'}

controlador = 0
numero_termos = 11
total = 0

print('\n',' '*27,f'{colors["Purple"]}Desenvolvendo uma Progressão Aritmética{colors["Clean"]}\n')

# ------------ Informações iniciais ---------------

numero_inicial = int(input('\n{}Informe um número para iniciar -->{} '.format(colors['Gray'],colors['Blue'])))

razao_pa = int(input('{}Informe a razão da P.A -->{} '.format(colors['Gray'],colors['Blue'])))
print(f'{colors["Clean"]}')

# ------------- Estrutura de decisão --------------

# --> O laço vai continuar até que o controlador e o número de termos sejam iguais.

while controlador < numero_termos:

    controlador += 1

    if controlador == 1:
        total = numero_inicial
        print('\n{}Termo'.format(colors['Green']), f'{controlador} -->',f'{colors["Yellow"]}',total)

    elif controlador == numero_termos:
        
        continuacao_termos = int(input('\n\n{}Deseja saber mais termos? \n(informe mais quantos termos deseja saber ou informe zero para encerrar) \n\n--->{} '.format(colors['Gray'],colors['Blue'])))

        if continuacao_termos == 0: #condição que permite sair do laço caso o usuário digite 0.
            numero_termos = 0

        else: #condição que aumenta o número de termos e ele deixa de ser igual ao controlador.
            numero_termos += continuacao_termos + 1     
    
    else:
        total += razao_pa
        print(f'{colors["Green"]}Termo' , f'{controlador} -->{colors["Yellow"]}',total)

print('\n\n',' '*27,f'{colors["Purple"]}Fim!{colors["Clean"]}\n\n')

#Na segunda parte que é a continuação dos termos o contador dos termos apresenta a continuação pra mais, pois considera a pergunta.

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.