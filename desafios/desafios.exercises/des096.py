def layout(caracterie, msg):  
    print(f'{caracterie}'*27)
    print(' '*36,msg)
    print(f'{caracterie}'*27)


def area(width, height):    
    total = width * height
    layout('---', f'The area has {total:.2f} m².')


layout('===', 'Rectangular area')

wid = float(input('>>> Enter a value to width (m): '))
hei = float(input('>>> Enter a value to height (m): '))

area(wid, hei)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.