print()
print('==='*27)
print('\n',' '*27,'Purchasing control\n') #controle de compras
print('==='*27)

control = total = sum_of_products = 0

lowest_priced_product = lowest_price = 0

boolean = False

while boolean != True:

    control += 1

    while True:

        product = str(input(f'\n--> Enter the name of the {control}st product: ')).strip()

        if product[:3].isalpha() == True:
            break
        else:
            print('~~~'*27)
            print('\n[Alert]The product name cannot start with numbers.\n') #Ñ é permitido o nome do produto começar com num.
            print('~~~'*27)
    
    while True:

        try:
            print('==='*27)
            price = float(input(f'\n--> Inform the price of the {control}st product: u$ '))
            print('==='*27,'\n')

            if price <= 1 or price > 71000:
                print('~~~'*27)
                print("\nThis value isn't accepted.\n\nAllowed values between U$ 1 and U$ 71000")
                print('~~~'*27,'\n')
            
            else:
                break

        except:
            print('~~~'*27)
            print('\n[Alert] Enter a numerical value.\n')
            print('~~~'*27)
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

        to_be = str(input('\n--> Want to continue? [Y/N]')).strip().lower()[0]
        print('\n','==='*27)

        if to_be == 'n':
            boolean = True
            break
        elif to_be == 'y':
            break
        else:
            print('==='*27)
            print("\n[Alert] Unidentified answers ('y' to yes or 'n' to not)\n")
            print('==='*27)
print('---'*27)
print(f'\n>>> Total expenses US {total}.\n')
print(f'\n>>> {sum_of_products} products above US 1.000 were identified.')
print(f'\n>>> The cheapest product was: --> {lowest_priced_product}\n')
print('---'*27)
            
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.