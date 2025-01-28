import os

def layout(caracter, numero_multiplicador, msg):
    print(f'{caracter}'*36)
    print(f' '*numero_multiplicador, f'{msg}')
    print(f'{caracter}'*36)

def tabuada(numero):
    print('=-'*36)
    for c in range(0, 11):
        print(' '*16 ,f'{numero} x  {c:<2}  =  {numero*c:>}')
    print()
    print('=-'*36)

def usuario():
    while True:
        try:
            teste = float(input('    >>> Informe um número: '))
            if teste.is_integer():
                return int(teste)
            else:
                print()
                print(f'O número digitado {teste} foi convertido para {round(teste)}')
                print()
                return round(teste)
        except ValueError:
            layout('---', 9, '[Erro] Tente novamente!! ')

def limpar():
    os.system('cls')

def continuar():
    while True:
        resposta = str(input('>>> Você quer continuar? (Aperte S para sim ou qualquer tecla para concluir) ')).lower()
        if resposta and resposta[0] == 's':
            limpar()
            main()
        else:
            layout('===', 36, ' Programa Concluido com Sucesso!!')
            exit()

def main():
    layout('===', 36, ' Tabuada ')
    print()
    numero_do_usuario = usuario()
    tabuada(numero_do_usuario)
    continuar()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.