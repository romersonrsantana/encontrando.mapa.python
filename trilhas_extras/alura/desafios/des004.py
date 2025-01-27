def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36, f'{msg}')
    print(f'{caracter}'*36)


def obter_eixo_x():
    tentativa = 0

    while tentativa < 4:
        try:
            return int(input('>>> Informe o eixo X: '))
        
        except ValueError:
            tentativa += 1
            print(f'\n       Informe um valor numerico (alerta para {tentativa}° tentativa): ')
            print()
            if tentativa == 3:
                mensagem_encerramento_tentativas()
                exit()


def obter_eixo_y():
    tentativa = 0

    while tentativa < 4:
        try:
            return int(input('>>> Informe o eixo Y: '))
        except ValueError:
            tentativa += 1
            print(f'\n Informe um valor numerico (alerta para {tentativa}° tentativa): ')
            print()
            if tentativa == 3:
                mensagem_encerramento_tentativas()
                exit()


def mensagem_encerramento_tentativas():
    layout('---', f'Você atingiu o número de tentativas!\nPrograma Encerrado!')

def coordenadas(x, y):
    match(x, y):
        case _ if x > 0 and y > 0:
            return 'Valores no primeiro quadrante!'
        case _ if x < 0 and y > 0:
            return 'Valores no segundo quadrante!'
        case _ if x < 0 and y < 0:
            return 'Valore no terceiro quadrante!'
        case _ if x > 0 and y < 0:
            return 'Valores no quarto quadrante!'
        case _ :
            return 'Valores no eixo origem!'
        

def main():
    layout('===', 'Coordenadas X e Y')
    test = coordenadas(obter_eixo_x(), obter_eixo_y())
    layout('---', test)
    print()


if __name__ == '__main__':
    main()


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.