import pprint
count = {}

def art():
    print('\n'*3)

mensage = 'It was a bright cold day in April, and the clocks were strinking thirteeen.'

for c in mensage:
    count.setdefault(c, 0) #defini um valor para a chave que está em c.
    count[c] = count[c] + 1

art()
print(count)
art()
pprint.pprint(count) #coloca em ordem alfabetica, em cada linha.
art()
print(pprint.pformat(count))