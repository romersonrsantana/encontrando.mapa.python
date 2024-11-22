import re

def layout(information, txt):
    print('---'*27)
    print(' '*7,f'{information}: ',f'{txt}')
    print('---'*27,)

padrao_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = padrao_regex.search('My number is 415-555-4242')
layout('Group complet',mo)
layout('code area',mo.group(1))
#If you want to obtain the groups in tuple format .groups
layout('Using the groupby method', mo.groups())
#Using multiple assignment
area_code, number = mo.groups()
layout('Area code in tuple', area_code)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.