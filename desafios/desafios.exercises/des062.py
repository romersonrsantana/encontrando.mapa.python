controlador = 0
numero_termos = 11
total = 0

print()

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
        controlador = 0
        continuacao_termos = int(input('\n\nDeseja saber mais termos? \n(informe mais quantos termos deseja saber) \n\n---> '))

        if continuacao_termos == 0:
            numero_termos = 0
        else:
            numero_termos += continuacao_termos
    
    else:
        total += razao_pa
        print('Termo' , f'{controlador} -->',total)

print('\n\nFim!\n\n')


'''while controlador < numero_termos and numero_termos != 0:

    controlador += 1

    if controlador == 1:
        total = n
        print(total)

    elif controlador == numero_termos:
        continuacao_termos = int(input('Deseja saber mais termos?'))

        controlador = 0
        numero_termos = continuacao_termos

        while controlador < continuacao_termos:
            
            controlador += 1
            
           

            if continuacao_termos != 0:
                total += r
                print(total)
                
            elif continuacao_termos == controlador:  
                continuacao_termos = int(input('Deseja saber mais termos --> '))
            
            #else:
                #print('\n\nFim!!\n\n') 
                continuacao_termos = int(input('Deseja saber mais termos --> '))

    else:
        total += r
        print(total)'''
    
    

