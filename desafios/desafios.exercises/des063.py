print('Sequencia de fibonacci')

proxima_sequencia = 0
contador = 0
total = 0
anterior = 0
anterior_2 = 0

proxima_sequencia = int(input('\nInforme quantos números da sequência de Fibonacci você gostaria de ver --> '))

while contador < proxima_sequencia:

    contador += 1 
    
    if contador == 1:
        anterior = 1
        print(anterior, end = ' -> ')
    
    elif contador == 2:
        anterior_2 = 1
        print(anterior_2, end = '-> ')

    elif contador == 3:
        anterior_3 = anterior + anterior_2
        print(anterior_3, end = '--> ')
    
    else:
        total = anterior_3 + anterior_2
        print(total, end ='--> ')
        anterior_2 = anterior_3
        anterior_3 = total

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém. Obrigado Jesus!!! Não sou Nada sem Ti. Amém.

    



