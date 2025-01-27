import os
#Variáveis
restaurantes = list()

#Usando Fsymbols

def menu_titulo():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")
    
def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36,f'{msg}')
    print(f'{caracter}'*36)
    print()

def tecla_retorno():
    layout('===','Aperte uma tecla para voltar ao menu principal: ')
    input()
    os.system('cls')

def titulo_da_escolha(titulo):
    os.system('cls')
    layout('---',f'{titulo}')

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
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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

def cadastrar_restaurante():
    titulo_da_escolha('Cadastro de restaurante')
    restaurante = str(input('>>> Informe o nome do restaurante: '))
    restaurantes.append(restaurante)
    layout('...', 'Restaurante Cadastrado com Sucesso!')

    escolha = str(input('>>> Digite S para cadastrar um novo restaurante ou outra tecla para voltar ao Menu Principal: ')).lower()[0]

    if escolha == 's':
        cadastrar_restaurante()
    else:
        main()

def listar_restaurantes():
    titulo_da_escolha('Lista de restaurantes')
    if len(restaurantes) > 0:
        for c in restaurantes:
            print(f'--> {c} ')
        print()
        tecla_retorno()
        main()
    else:
        layout('===', 'Não há restaurantes cadastrados')
        tecla_retorno()
        main()

#inicio programa
#função que controla o projeto
def main():
    menu_titulo()
    menu_escolha()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor JeSUS Cristo, Para Sempre Seja Louvado. Amém.