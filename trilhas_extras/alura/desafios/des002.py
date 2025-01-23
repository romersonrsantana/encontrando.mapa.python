def titulo():
    print()
    print("""                    🆅 🅴 🆁 🅸 🅵 🅸 🅲  🅰  🅳 🅾  🆁                 """)
    print()

def layout(caractere, msg):
    print(f'{caractere}'*36)
    print(' '*36, f'{msg}')
    print(f'{caractere}'*36)


def verificar(idade):
    match idade:
        case _ if  idade >= 0 and idade <= 12:
            layout('---', 'Criança!')
        case _ if  idade >= 13 and idade <= 18:
            layout('---', 'Adolescente!')
        case _ if idade > 18 and idade <= 120:
            layout('---', 'Adulto!')
        case _ :
            layout('---', 'Não corresponde a idade de umm ser humano!')

titulo()


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.