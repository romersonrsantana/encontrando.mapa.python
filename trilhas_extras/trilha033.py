print('==='*27)
print(' '*27,'Character Count')
print('==='*27)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for c in message:
    count.setdefault(c, 0)

    count[c] = count[c] + 1  #de inicio I é igual a zero, depois a chave é mantida e o valor dela é somada mais um quando essa mesma chave aparece.

for key, value in count.items():
    print(f'\n--> Character: {key:-^9} Amount: {str(value)}')

#Toda Honra e Toda Glória Ao Pai Celestial Papai do Céu Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.