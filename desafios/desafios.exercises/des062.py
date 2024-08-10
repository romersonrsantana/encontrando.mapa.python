controlador = 0
numero_termos = 11
total = 0

print()
n = int(input('--> '))
r = int(input('--> '))



while controlador < numero_termos and numero_termos != 0:

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
            
            else:
                print('Fim!!')

            

    else:
        total += r
        print(total)
    
    

