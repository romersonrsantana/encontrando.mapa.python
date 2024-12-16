import re

def layout(msg):
    print('==='*27)
    print(' '*36,msg)
    print('==='*27)


def scan(resp):
    print()
    print(f' >>> {resp}')
    print()

layout('Opcional match using (?) ')

bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The adventures of Batwoman and Batman')

scan(mo1.group()) #A preferência é Batwoman, caso não ouvesse seria imprimido Batman.
scan(mo1)

layout('Example with area code')
phone_regex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo2 = phone_regex.search('My number is 555-7172')
scan(mo2.group())
scan(mo2)

layout('Occurences using asteridco')

bat_regex = re.compile(r'(Bat)*woman') #Número indeterminado de ocorrências
mo3 = bat_regex.search('The adventures of BatBatwomanwonwowowoman')

if mo3 == None:
    scan('Value not found!')
else:
    scan(mo3.group())
    scan(mo3)


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.