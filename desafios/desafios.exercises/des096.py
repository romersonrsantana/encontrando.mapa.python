def layout(caracterie, msg):  
    print(f'{caracterie}'*27)
    print(' '*36,msg)
    print(f'{caracterie}'*27)


def area(width, height):
    return width * height


layout('===', 'Rectangular area')

width = float(input('>>> Enter a value to width (m): '))
height = float(input('>>> Enter a value to height (m): '))

total = area(width, height)

layout('---', f'The area has {total:.2f} m².')


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.