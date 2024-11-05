print('---'*27)
print(' '*27,' Fantasy Inventory ')
print('---'*27)

def adicionando_inventario(inventory, add_to_items):

    for c in add_to_items:

        inventory.setdefault(c, 0)

        inventory[c] = inventory[c] + 1

def layout(chaves):
    total = 0

    for k, v in chaves.items():
        print(f'   >>> Item {k} : {v}.')
        total += v
        print()

    print(f'>>> Total de itens {total}.')
    print()

inventario = {'gold coin': 42, 'rope': 1}

resultado = ['gold coin', 'dagger', 'gold coin', 'tesj', 'gold coin', 'ruby']

adicionando_inventario(inventario, resultado)
layout(inventario)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.