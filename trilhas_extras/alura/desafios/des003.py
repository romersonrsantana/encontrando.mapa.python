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

    tentativa = 0
    maxima_tentativas = 4

    while tentativa < maxima_tentativas:
        login = obter_usuario()
        senha = obter_senha()
         
        match (login, senha):

            case _ if dados_login == login and dados_senha == senha:
                print("""
                  
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄
                  """)
                break

            case _ if tentativa == 2:
                print()
                print(f'[Alert] Número máximo de tentativas atingido. Acesso bloqueado.')
                print()
                break
        
            case _ if dados_login != login or dados_senha != senha:
                    tentativa += 1
                    print(f"""[Erro]​​​​ Informe novamente! {tentativa} de {maxima_tentativas - 1}""")
                    print()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.