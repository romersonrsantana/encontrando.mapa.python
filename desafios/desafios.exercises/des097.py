def layout(caractere, title):
    print(f'{caractere}'*36)
    print(' '*43,f'{title}')
    print(f'{caractere}'*36)

def write(mensage, items):
    print(f'{items}')
    print(f'   {mensage}')
    print(f'{items}')


mens = str(input('Write a mensage: >>> '))
i = '-' * (len(mens) + 6)  
layout('===', 'Responsive')
write(mens, i)


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.