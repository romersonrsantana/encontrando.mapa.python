print('==='*27)
print(' '*36,'Display Inventary')
print('==='*27)

inventary_player = dict()

key_name = 0
value_name = 0
control  = False

while True:
    
    key_name = str(input('>>> Enter one item name: (or enter to exit) '))
    
    if key_name == '':
       break
  
    value_name = int(input('>>> Inform the quantity: (or 0 to exit) '))

    if value_name == 0:
        break

    inventary_player[key_name] = value_name

print(inventary_player)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.