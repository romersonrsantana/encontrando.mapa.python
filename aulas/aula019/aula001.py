print('==='*27)
print(' '*36,'New subject')
print('==='*27,'\n')

pessoas = {'nome': 'Tereza', 'sexo':'Feminino' ,'idade': 55}

print(pessoas)

print('\n', 'João e ',pessoas['nome'],'.')

print('\n',f'{pessoas["nome"]} have {pessoas["idade"]} years old.','\n')

print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()

pessoas['peso'] = 69

for k in pessoas.keys():
    print(k)

print()

for v in pessoas.values():
    print(v)

print()

for k, v in pessoas.items():
    print(f'{k} = {v}. ')

print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.