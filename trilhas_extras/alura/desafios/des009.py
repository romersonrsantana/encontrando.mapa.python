import os
lista_de_numeros = list()


def layout(caracter, numero_multiplicador, msg):
    print(f'{caracter}'*36)
    print(' '*numero_multiplicador,f'{msg}')
    print(f'{caracter}'*36)

def incluindo_numeros():
    while True:
        try:
            return int(input('>>> Quantos números deseja incluir? '))
        except:
            layout('===', 27, 'Informe um número inteiro... ')

def solicitacao_usuario():
    contador = 0
    quant_de_numeros = incluindo_numeros()

    while contador < quant_de_numeros:
        try:
            numero = float(input('>>> Informe o número: '))
            if len(lista_de_numeros) == 0:
                lista_de_numeros.append(numero)
                contador += 1
            else:
                if numero not in lista_de_numeros:
                    lista_de_numeros.append(numero)
                    contador += 1
                else:
                    layout('---', 36, '[Alert] Número já informado!')
        except ValueError:
            layout('---', 36, 'Informe um valor válido!')
    

def media():
    soma = 0
    try:
        for c, v in enumerate(lista_de_numeros):
            soma += v
        return layout('---', 27, f'Foram considerados {len(lista_de_numeros)} números, a média deles é {soma/len(lista_de_numeros):.2f}! ')
    except ZeroDivisionError:
        layout('===', 7, '[Alert] Não foi possível encontrar a média, A lista de números está vazia! ')

def continuar():
    escolha = str(input('>>> Gostaria de inserir outros números? (aperte s para continuar ou qualquer outra tecla para encerrar) ')).lower()
    if escolha and escolha[0] == 's':
        limpar()
        main()
    else:
        layout('===', 36, 'Programa Encerrado com Sucesso!')
        print()
        exit()

def limpar():
    lista_de_numeros.clear()
    os.system('cls')

def main():
    layout('===', 36, '     Média   ') 
    solicitacao_usuario()
    media()
    continuar()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.