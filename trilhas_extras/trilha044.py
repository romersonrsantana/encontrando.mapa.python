#Sagrado Coração de Jesus Confio e Espero em Vós. Amém.

def layout(msg, caractere):
    print(f'{caractere}'*27)
    print(' '*36,f'{msg}')
    print(f'{caractere}'*27)

def is_phone_number(text):
    if len(text) != 12:
        return False
    for c in range(0,3):
        if not text[c].isdecimal():
            return False
    if text[3] != '-':
        return False
    for c in range(4, 7):
        if not text[c].isdecimal():
            return False
    if text[7] != '-':
        return False
    for c in range(8, 12):
        if not text[c].isdecimal():
            return False
    return True
        
layout('Identifying phone number', '===')
print('Result')
layout(f'''415-555-4242 is a phone number? >>> {is_phone_number('415-555-4242')}''','---')
print('Second test')
layout(f'''Moshi moshi is a phone number? >>> {is_phone_number('Moshi moshi is a phone number? ')}''', '---')
print()

# Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moises e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém. 