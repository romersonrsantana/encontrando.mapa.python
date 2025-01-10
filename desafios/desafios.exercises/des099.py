def layout(n, mensage):
    print(f'{n}'*36)
    print(' '*36, f'{mensage}')
    print(f'{n}'*36)

def bigger(*number):
    for c, v in enumerate(number):
        if c == 0:
            big_number = v
        else:
            if v > big_number:
                big_number = v
    print(f'The big number was {big_number}')

layout('===', 'Te Amo Mamãe Tereza')

layout('===', 'Bigger function')

bigger(5, 9, 16, 36, 28)

bigger(16, 28, 6, 7, 2, 9)

number_val = list()

while True:

    n = int(input('Enter a name or (enter 0 to stop) >>> '))

    if n == 0:
        bigger(*number_val)
        break
    else:
        number_val.append(n)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.