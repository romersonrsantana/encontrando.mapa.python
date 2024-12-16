import re 

def layout(mensage, caractere):
    print(f'{caractere}' * 36)
    print(' '*36, f'{mensage}')
    print(f'{caractere}' * 36)


def test(regex_find):
    if regex_find == None:
        layout('Regex not found', '~~~')
    else:
        layout(regex_find.group(), '---')

greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHaHaHa')
test(mo1)

nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_ha_regex.search('HaHaHaHaHaHaHaHa')
layout('Nongreedy Regex','===')
test(mo2)

#Toda Honra e Toda Glória Ao Deus de Abraão, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Noso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.