print('\nDiscovering the factorial\n')

factorial = 3

usuario = float(input('\nIndique um número para iniciar: --> '))
print()

inicio = usuario

while factorial > 1:

    factorial = usuario - 1

    if inicio == usuario:
        total = (inicio * factorial)

        print(usuario, ' x ', end='')
        print(factorial, ' x ', end='')

    elif factorial == 1:
        total = total * factorial

        print(factorial, ' = ', end='')

    else:
        total = total * factorial

        print(factorial, ' x ', end='')
    
    usuario = usuario - 1

print(total)
print('\n')
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espirito Santo. Toda Honra e Toda Glória a Jesus Cristo. Amém. 