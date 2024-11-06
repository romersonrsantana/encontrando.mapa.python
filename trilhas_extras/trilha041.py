print(' center '.center(88,'-'))

def layout_picnic(items_dictionary, left_width, rigth_width):
    print(' Picnic Items '.center(left_width + rigth_width, '-'))

    for k, v in items_dictionary.items():
        print(f'>>> {k.ljust(left_width,'.')}' + f'{str(v).rjust(rigth_width)}')

dictionary_picnic = {'sandwiches': 4, 
                    'apples': 12,
                    'cups': 4,
                    'cookies': 8000}

layout_picnic(dictionary_picnic, 16, 12)
print()
print('==='*27)
print()
layout_picnic(dictionary_picnic, 28, 16)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.