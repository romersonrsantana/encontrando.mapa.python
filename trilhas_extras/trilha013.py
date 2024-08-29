print('\nTesting global variables!\n')

def calling():
    global spam     #como spam é declarada como global, a atribuição de spam é feita no escopo global.
    spam = '\neggs\n'
    print(spam)

spam = 'global'
calling()
print(spam)

"""
1. Se uma variável estiver sendo usada no escopo global(ou seja, fora de todas as funções), ela será sempre uma variável global.
2. Se houver uma instrução global para essa variável em uma função, ela será uma variável global.
3.Caso contrário, se a variável for usada em uma instrução de atribuição na função, ela será uma variável local.
4.Porém, se a variável não for usada em uma instrução de atribuição, ela será uma variável global."""