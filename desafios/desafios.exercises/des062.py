colors = {'Purple':'\033[m',
          'Blue':'\033[m',
          'Yellow':'\033[m',
          'Green':'\033[m',
          'Alert':'\033[m',
          'Gray':'\033[m',
          'Clean':'\033[m'}

controlador = 0
numero_termos = 11
total = 0

print('\n',' '*27,'Desenvolvendo uma Progressão Aritmética\n')

# ------------ Informações iniciais ---------------

numero_inicial = int(input('\nInforme um número para iniciar --> '))

razao_pa = int(input('Informe a razão da P.A --> '))

# ------------- Estrutura de decisão --------------

# --> O laço vai continuar até que o controlador e o número de termos sejam iguais.

while controlador < numero_termos:

    controlador += 1

    if controlador == 1:
        total = numero_inicial
        print('\nTermo', f'{controlador} -->',total)

    elif controlador == numero_termos:
        
        continuacao_termos = int(input('\n\nDeseja saber mais termos? \n(informe mais quantos termos deseja saber ou informe zero para encerrar) \n\n---> '))

        if continuacao_termos == 0: #condição que permite sair do laço caso o usuário digite 0.
            numero_termos = 0

        else: #condição que aumenta o número de termos e ele deixa de ser igual ao controlador.
            numero_termos += continuacao_termos + 1      
    
    else:
        total += razao_pa
        print('Termo' , f'{controlador} -->',total)

print('\n\nFim!\n\n')

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.