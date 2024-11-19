def is_phone_number(text):
    if len(text) != 12:
        return False
    for c in range(0, 3):
        if not text[c].isdecimal():
            return False
    if text[3] != '-':
        return False
    for c in range(4, 7):
        if not text[c].isdecimal(): #verifica se o caractere na posição c não é um decimal, exemplo de 0 a 9. Se isso for verdade ela retorna o código retorna False, indicando que algo falhou, ou não atende uma condição especifica.
            return False
    if text[7] != '-':
        return False
    for c in range(8, 12):
        if not text[c].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for c in range(len(message)):
    chunk = message[c : c + 12] #A cada iteração do loop for, uma nova porção de 12 caracteres de message é atribuida à variável chunk. Por exemplo, na primeira iteração, c será 0 e chunk receberá message[0:12] (ou seja, a string 'Call me at 4'). Na próxima iteração, c será 1 e chunk receberá message[1:13] (a string 'all me at 41').

    if is_phone_number(chunk):
        print(f'Phone number found: {chunk}')
print('done')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.