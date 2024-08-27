colors = {'blue':'\033[1;34m',
                'purple':'\033[1;35m',
                'alert':'\033[1;31m',
                'gray':'\033[1;37m',
                'clean':'\033[m'}



print('\n',' '*27,f'{colors["purple"]}Multiplication table!{colors["clean"]}\n')

total = counter = 0

while True:
    try:
        number = int(input(f'\n{colors["gray"]}Enter an interger:\n\n-->{colors["blue"]} '))

        if number == 999:
            break
        
        counter += 1
        total += number

    except:
        print('\n{}[Alert]{} Enter a valid number!{}\n'.format(colors['alert'], colors['gray'], colors['clean']))
    continue

print(f'\n{colors["blue"]}-->{colors["purple"]} {counter} {colors["blue"]}numbers were added,\n\n--> Total sum {colors["purple"]} {total} {colors["blue"]}.{colors["clean"]}\n\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.