
print(' Tempo de Chuva \n\n')

resposta = 1


while resposta != 2:

    print('''\nComo está o tempo hoje?
      
        (Informe o número correspondente)

            1 - Está chovendo
            2 - Não está chovendo''')
    try:
        resposta = int(input('--> '))
    except:
        print('\n[ALERT!] Digite números válidos!\n')
        continue
    if resposta < 1  or resposta > 2:
        print('\n[Alert] Opção inexistente\n')
    elif resposta == 1:
        try:
            resposta = int(input('\nVocê tem guarda chuva? (1 -Não, 2 - Sim )\n'))
        except:
            print('\n[Alert!]Valor inexistente!\n')
            continue
        if resposta == 1:
            print('\nEspere!')
        while resposta != 2:
            try:
                resposta = int(input('\nEstá chovendo? (1 - Sim, 2 - Não) --> '))
            except:
                print('\n[Alert!] Valor inexistênte!\n')
                continue
            if resposta == 1:   
                print('\nEspere!\n')
            elif resposta == 2:
                print('\nSaia!\n')
            else:
                print('\nOpção inexistente!\n')

    #como chamar a função para voltar para o laço original?

    elif resposta == 2:
        print('\nVocê poderá sair de casa.\n')

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.
