print('==='*27)
print(' '*36,'Basedate')
print('==='*27)

brasil = list()
state = dict()

for c in range(0,3):
    state['uf'] = str(input('Enter a name of the state: '))
    state['sigla'] = str(input('Enter a sigla: '))
    brasil.append(state.copy())

    print()

print(brasil)
print()

for c in brasil:
    print(c)

print()

for c in brasil:
    for v in c.values():
        print(F'{v} ', end='')
    print()

print()
#Te Amo Papai do Céu, Te Amo Espírito Santo, Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.