print('\n\n Bem Vindo(a)!! \n\n Aqui vamos calcular o Preço da passagem por KM de distância... \n\n')
distancia = int(input('Informe a distância em KM da viagem desejada: '))
if distancia > 15474:
    print('\n\n [INFORME OUTRO VALOR!!]. \n\nO valor informado ultrapassou o registro de viagem mais longa que é possivel de ser realizada.\n\n Considerando a viagem de avião de New York para Singapura. Com um total de 15.474km.\n\n')
else:
    if distancia < 200:
        print('\n\n Para esse trajeto será cobrado R$ 0,50 centavos por KM. Portanto: \n\n ---> {} x R$ 0.50 = R$ {:.2f} reais.\n\n'.format(distancia, (distancia*0.50)))
    else:
        print('\n\n Para esse trajeto será cobrado R$ 0.45 centavos por KM. Portanto: \n\n --- {} x R$ 0,45 = R$ {:.2f} reais.\n\n'.format(distancia, (distancia*0.45)))