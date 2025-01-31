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
    while contador < quant_de_numeros:
        try:
            numero = int(input('>>> Informe o número: '))
            if len(lista_de_numeros) == 0:
                lista_de_numeros.append(numero)
                contador += 1
            else:
                if numero not in lista_de_numeros:
                    lista_de_numeros.append(numero)
                contador += 1
        except ValueError:
            layout('---', 36, 'Informe um valor válido!')


quant_de_numeros = incluindo_numeros()
solicitacao_usuario()
print(lista_de_numeros)
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.