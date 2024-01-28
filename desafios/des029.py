print('\n----- Controle de velocidade -----\n\n')
veloc = int(input('Informe a velocidade que passou em uma via com o limite máximo permitido de 80km:  '))
if veloc >= 301:
    print('\n\n Reescreva o valor, provavelmente você não conseguiria atingir essa velocidade, nas rodovias brasileiras, se atingiu... DEVERIA SER PRESO!!\n\n')
else:
    if veloc == 0:
        print('\n\n Seu veiculo está PARADO!!\n\n')
    else:
        if veloc <= 4:
            print('\n\n Ande no acostamento!! Pois sua velocidade está muito abaixo da velocidade da via, o que pode provocar um acidente!!\n\n')
        else:
            if veloc <= 80:
                print('\n\n A velocidade está dentro dos limites permitidos!!\n\n')
            else:
                print('\n\n Você foi multado!! A multa será de R$ 7,00 por cada km/h acima do permitido, \n\n considerando: \n\n A velocidade informada de: {} km/h. \n\n O limite ultrapassado foi de: {}km/h \n\n Sua multa será de R$ {} reais \n\n'.format(veloc, (veloc - 80), (veloc-80)*7 ))