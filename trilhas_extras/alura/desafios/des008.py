import os

lista_de_numeros = list()

def layout(caracter, number, msg):
    print(f'{caracter}'*36)
    print(f' '*number, f'{msg}')
    print(f'{caracter}'*36)

def solicitar_numeros():
    global lista_de_numeros
    while len(lista_de_numeros) <= 2:
        try:
            item = float(input('>>> Informe um número: '))
            if item.is_integer():
                lista_de_numeros.append(int(item))
                layout(' ', 36, 'Número adicionado! ')
            else:
                arredondado = round(item)
                layout('---', 27, f'--> O número {item} foi arrendondado para {arredondado}... ')
                lista_de_numeros.append(arredondado)
                layout(' ', 36, 'Número adicionado! ')
        except ValueError:
            layout('---', 36, '[Alert] Digite números!')

def somar():
    soma = 0
    for c, valor in enumerate(lista_de_numeros):
        soma += valor
    layout('---', 36, f' Valores Somados {soma}! ')
    lista_de_numeros.clear()

def limpar():
    os.system('cls')


def continuar():
    pergunta = str(input('>>> Você quer continuar? (aperte s para sim ou qualquer tecla para encerrar) ')).lower()
    if pergunta and pergunta[0] == 's':
        limpar()
        main()
    else:
        layout('===', 36, 'Programa Encerrado!')
        exit()

def main():
    layout('===', 36, 'Somando Números Inteiros')
    solicitar_numeros()
    somar()
    continuar()


if __name__ == '__main__':
    main()
    continuar()


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.