print('==='*27)
print(' '*27,'Identifying Vowels')
print('==='*27)

words = ('soccer', 'football', 'child', 'sugar', 'computer', 'gibbs', 'toni', 'ziva', 'maggi', 'candice', 'antuani')

vogais = 'aeiou'

for c in words:
    print(f'\nIn {c:.^18} has vowels --> ', end='')

    if 'a' in c:
        print('a ', end='')
    if 'e' in c:
        print('e ', end='')
    if 'i' in c:
        print('i ', end='')
    if 'o' in c:
        print('o ', end='')
    if 'u' in c:
        print('u', end='')
    print()

print('==='*27)
print(' '*18,'Program completed successfully! Thanks!')
print('==='*27)

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés Ao Seu Espírito Santo E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.