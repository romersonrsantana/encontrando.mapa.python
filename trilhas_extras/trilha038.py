print('==='*27)
print(' '*36,'Display Inventary')
print('==='*27)

inventary_player = dict()

key_name = 0
control  = False

def display(parametro_for):
    print('---'*27)
    print(' '*36,'Control')
    print('---'*27)
    cont = 0

    for k, v in parametro_for.items():
        print(f'    >>> The item {k} : values {v}.')
        cont += v
        print()

    print(f'>>> Total itens {cont}')

while True:
    
    key_name = str(input('>>> Enter one item name: (or enter to exit) '))
    
    if key_name == '':
       break
  
    inventary_player[key_name] = int(input('>>> Inform the quantity: '))

display(inventary_player)
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.