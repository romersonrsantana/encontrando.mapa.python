all_guess = {'Alice':{'apples': 5, 'pretzels': 12}, 
             'João':{'ham sandwiches': 3, 'apples': 2 },
            'Tereza':{'cups': 3, 'apple pies': 4}}

def total_brought(guess, item):
    num_brought = 0

    for k, v in guess.items():
        num_brought += v.get(item, 0)
    return num_brought

#faz a iteração pelos pares chave-valor em guess, a string com o nome do convidado é atribuida a k. E o dicionário de itens de piquinique é atribuida a v. Se o parâmetro referente ao item estiver presente como uma chave nesse dicionário, seu valor será somado a num_brought.

print('Number of things being brought: ')

print('--> Apples  ' + str(total_brought(all_guess, 'apples')))
print()
print('--> Cups  ' + str(total_brought(all_guess, 'cups')))
print()
print('--> Cakes  ' + str(total_brought(all_guess, 'cakes')))
print()
print('--> Ham Sandwiches  ' + str(total_brought(all_guess, 'ham sandwiches')))
print()
print('--> Apple Pies  ' + str(total_brought(all_guess, 'apple pies')))
print()
print('--> Orange  ' + str(total_brought(all_guess, 'oranges')))
print()

#Toda Honra e Toda Glória A Papai do Céu, Deus de Abrãao, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.