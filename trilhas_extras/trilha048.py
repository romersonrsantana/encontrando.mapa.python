import re

def layout(mensage, resultado):
    print()
    print(f'>>> {mensage} : {resultado}.')
    
print('==='*36)
print(' '*36,'Pipe')
print('==='*36)

hero_regex  = re.compile(r'Batman | Tina Fey | A')
mo1 = hero_regex.search('Batman and Tina Fey.')
mo2 = hero_regex.search('Batma jklm Tina Fe A')

hero_regex_1 = re.compile(r'Bat(man|mobile|co)')
mo3 = hero_regex_1.search('ldsldhfhd Batmobile ... ')

layout(mo1, mo1.group())
layout(mo2, mo2.group())
layout(mo3, mo3.group())
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.