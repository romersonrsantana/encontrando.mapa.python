number = 1
soma_par = soma_impar = 0

while number != 0:

    try:
        number = int(input('\nDigite um número: '))
        if number != 0:
            if number % 2 == 0:
                soma_par += 1
            else:
                soma_impar += 1
    except:
        print('\n\n --> Você digitou caracteres não númericos!\n[ALERT!!] Valor não considerado!!\n')
        continue

if soma_impar > soma_par:
    print('\nA quantidade de números impares venceu!!\n')
elif soma_impar == soma_par:
    print('\nEmpate de números impares e pares digitados!!\n')
else:
    print('\nA quantidade de números pares venceu!!\n')

print(f'Quantidade digitada: \n\n--> {soma_impar} \n\n -->{soma_par}\n\n')
#Jesus confio e espero em Ti. Amém.