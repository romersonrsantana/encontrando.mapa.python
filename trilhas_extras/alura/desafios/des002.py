def titulo():
    print()
    print("""                    🆅 🅴 🆁 🅸 🅵 🅸 🅲  🅰  🅳 🅾  🆁                 """)
    print()


def layout(caractere, msg):
    print(f'{caractere}'*36)
    print(' '*36, f'{msg}')
    print(f'{caractere}'*36)


def usuario():
    while True:
        try:
            print()
            return int(input('>>> Informe sua idade: '))
        
        except ValueError:
            print()
            print('     [Alert] Informe um valor númerico.')



def verificar(idade):
    match idade:
        case _ if  idade >= 0 and idade <= 12:
            layout('---', 'Criança!')
        case _ if  idade >= 13 and idade <= 18:
            layout('---', 'Adolescente!')
        case _ if idade > 18 and idade <= 120:
            layout('---', 'Adulto!')
        case _ :
            layout('---', 'Não corresponde a idade de um ser humano!')
            print()
            verificar(usuario())


#Principal
def main():
    titulo()
    verificar(usuario())
    

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.