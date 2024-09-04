print('\nPurchasing control\n') #controle de compras

control = total = sum_of_products = 0

lowest_priced_product = lowest_price = 0

boolean = False

while boolean != True:

    control += 1

    while True:

        product = str(input(f'\nEnter the name of the {control}st product: ')).strip()

        if product[:3].isalpha() == True:
            break
        else:
            print('\nThe product name cannot start with numbers.\n') #Ñ é permitido o nome do produto começar com num.
    
    while True:

        try:
            price = float(input(f'\nInform the price of the {control}st product: u$ '))

            if price <= 1 or price > 71000:
                print("\nThis value isn't accepted.\n\nAllowed values between U$ 1 and U$ 71000")
            
            else:
                break

        except:
            print('\n[Alert] Enter a numerical value.\n')
            continue
    
    if price > 1000:
        sum_of_products += 1
    
    if control == 1:
        lowest_priced_product = product
        lowest_price = price

    elif price < lowest_price:
        lowest_priced_product = product
   
    total += price

    while True:

        to_be = str(input('\nWant to continue? [Y/N]')).strip().lower()[0]

        if to_be == 'n':
            boolean = True
            break
        elif to_be == 'y':
            break
        else:
            print("\n[Alert] Unidentified answers ('y' to yes or 'n' to not)\n")

print(f'\n>>> Total expenses US {total}.\n')
print(f'\n>>> {sum_of_products} products above US 1.000 were identified.')
print(f'\n>>> The cheapest product was: --> {lowest_priced_product}\n')
            
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.