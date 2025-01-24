def titulo():
    print("""
█░░ █▀▀█ █▀▀▀ ░▀░ █▀▀▄ 
█░░ █░░█ █░▀█ ▀█▀ █░░█ 
▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀""")

def obter_usuario():
    return str(input('  >>> Informe seu nome de usuário: '))


def obter_senha():
    return str(input('  >>> Informe sua senha: '))


#inicio
def main():
    titulo()

    dados_login = 'Tereza'
    dados_senha = '5655'

    login = obter_usuario()
    senha = obter_senha()

    match (login, senha):

        case _ if dados_login == login and dados_senha == senha:
            print("""
                  
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄
                  """)
        
        case _ if dados_login != login or dados_senha != senha:
                print("""[Erro]​​​​ Informe novamente!""")
                print()
                main()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.