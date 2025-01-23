import os

#Usando Fsymbols

def menu_titulo():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")


def menu_escolha():
    print('''
    1. Cadastrar Restaurante;
    2. Listar Restaurante;
    3. Ativar Restaurante;
    4. Sair;
      ''')
    
    try:
        opcao_escolhida = int(input('>>> Informe uma opção: '))

        if opcao_escolhida == 1:
            print(f'{opcao_escolhida}')
        elif opcao_escolhida == 2:
            print(f'{opcao_escolhida}')
        elif opcao_escolhida == 3:
            print(f'{opcao_escolhida}')
        elif opcao_escolhida == 4:
            print(f'{opcao_escolhida}')
        else:
            os.system('cls')
            print()
            print(f'        [Alert] Informe um valor aceito! Você digitou {opcao_escolhida}')
            menu_escolha()
    except:
        os.system('cls')
        print()
        print(f'        [Alert!] valor errado! Você digitou caracteres!')
        menu_escolha()

#inicio programa
#função que controla o projeto
def main():
    menu_titulo()
    menu_escolha()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor JeSUS Cristo, Para Sempre Seja Louvado. Amém.