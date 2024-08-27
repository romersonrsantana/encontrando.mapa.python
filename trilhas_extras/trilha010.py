print('\n\nTeste\n\n')

#As variáveis locais de uma função são completamente diferentes das variáveis locais de outra função. Vários escopos locais podem existir ao mesmo tempo.
def spam():         
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 711
    eggs = 0
    print(eggs)

spam()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó e Israel. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.