print('\n',' '*27,'Detalhando números')

controle = 'S'
contador = 0
total = 0
maior = 0
menor = 0
media = 0

while controle != 'n':

    contador += 1

    number = int(input('\nInforme um número --> '))
        
    if contador == 1:
        maior = menor = first_term = number

    else:
        if maior < number:
            maior = number

        elif maior > number:
            menor = number
    
        media += number

    controle = str(input('\nDeseja continuar? \n(Digite --> S para sim e --> N para Não)'))

    if controle != 'n' and controle != 's':
        print('\nComo não foi informado nenhuma das opções apresentadas, \nserá considerado que deseja informar mais valores!\n')

print(f'\nForam informados {contador} termos\n')
print(f'O maior termo é --> {maior}\n')
print(f'O menor termo é --> {menor}\n')

print(f'Média dos termos --> {media/contador}')

#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.