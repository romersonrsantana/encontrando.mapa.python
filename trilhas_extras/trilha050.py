import re

def layout(txt, caractere):
    print(f'{caractere}'*36)
    print(' '*36,f'{txt}')
    print(f'{caractere}'*36)


def test(return_regex):
    if return_regex == None:
        layout('There is not match', '---')
    else:
        layout(return_regex.group(), '---')

ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHaHa')
mo2 = ha_regex.search('Ha')

layout('Regex', '===')
test(mo1)
test(mo2)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.