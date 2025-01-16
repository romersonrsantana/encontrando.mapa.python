def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36,f'{msg}')
    print(f'{caracter}'*36)


def factorial(number, show=0):
    if show == 0:
        factorial = 1
        while number > 0:
            factorial *= number
            number -= 1
        return factorial
    else:
        factorial = 1
        while number > 1:
            print(f'{number} ', end='-')
            factorial *= number
            number -= 1
        print(f'{number}', end='')
        print()
        return factorial
        
test = factorial(5, 1)

print(f'The factorial is {test}')

#Toda Honra e Toda Glória Ao Deus de Abraão, Jacó, Israel e Moisés E Ao Seu Único Filho Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.