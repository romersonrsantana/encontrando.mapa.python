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
            print(f' {number} ', end='x')
            factorial *= number
            number -= 1
        print(f' {number} ', end='')
        print()
        return factorial
    

print()
num_factored = int(input('>>> Enter a number to be factored: '))

while True:
    print()   
    choise = int(input('>>> Report 0 to check the  total or 1 to check the factorial calculation: '))

    if choise == 0 or choise == 1:
        break
    else:
        print('[Alert] Report 1 or 2!')

layout('===', f'>>> The factorial of the number {num_factored} is: ')
print()
test = factorial(num_factored, choise)
print()
print(f'>>> {num_factored}! = {test} .')
print()
#Toda Honra e Toda Glória Ao Deus de Abraão, Jacó, Israel e Moisés E Ao Seu Único Filho Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.