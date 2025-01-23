def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36, f'{msg}')
    print(f'{caracter}'*36)

def imp_par(numero):
    match numero % 2:
        case 0:
            layout('---', 'O número é PAR!')
        case 1:
            layout('---', 'O número é ÍMPAR!')

def usuario():
    while True:
        try:
            print()
            return int(input('     >>> Informe um valor: '))
        except ValueError:
            print()
            print('Informe um valor númerico')

def main():
    layout('===', 'É par ou ímpar? ') 
    imp_par(usuario())   

#inicio do programa:
 
if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Único Filho Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.