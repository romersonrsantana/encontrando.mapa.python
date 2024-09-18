print('---'*27)
print(' '*27,'Palavras')
print('---'*27)

names = ('Deus','Espirito Santo','Jesus Cristo','Tereza', 'Joao',)

for c in names:
    print(f'\n{c:-^20} temos as vogais: ', end='')

    for letras in c:
        
        if letras.lower() in 'aeiou':
            print(f' {letras}.', end='')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés Ao Seu Espírito Santo E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.