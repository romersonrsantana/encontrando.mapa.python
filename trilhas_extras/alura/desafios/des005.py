import os

def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36, f'{msg}')
    print(f'{caracter}'*36)

def soma_impares(primeiro_intervalo, segundo_intervalo):
    total = 0
    for c in range(primeiro_intervalo, segundo_intervalo): 
        if c % 2 != 0:
            total += c
    layout('---', total)

def usuario():
    while True:
        try:
            return int(input('>>> Informe o numero do intervalo: '))
        except ValueError:
            layout('===', '[Alert] Digite um valor!')

def main():
    layout('===', 'Somando Números Impares')
    primeiro = usuario()
    segundo = usuario()
    while True:
        if primeiro < segundo:
            return soma_impares(primeiro, segundo)
        else:
            limpar()
            layout('---', f'O Segundo valor deve ser maior que o primeiro valor digitado que foi {primeiro}!')
            segundo = usuario()

def continuar():
    limpar()
    while True:
        try:
            resposta = str(input('>>> Você quer continuar? (Aperte S para sim ou qualquer outra tecla para encerrar) ')).lower()
            if resposta and resposta[0] == 's':
                limpar()
                main()
            else:
                layout('===', 'Programa Encerrado!')
                exit()
        except IndexError:            
            exit()

def limpar():
    os.system('cls')


if __name__ == '__main__':
    main()
    continuar()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.