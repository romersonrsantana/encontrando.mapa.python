import os

def layout(caractere, numero_multiplicador, msg):
    print(f'{caractere}'*36)
    print(' '*numero_multiplicador, f'{msg}')
    print(f'{caractere}'*36)

def leia_numero():
    while True:
        try:
            print('Digite um número inteiro: ')
            return float(input('>>> '))
        except ValueError:
            layout('---', 27, '[Alert] Digite um valor numérico!')

def main():
    layout('===', 36, 'Valores Numéricos')
    global numero 
    numero = leia_numero()
    resultado = verificar_numero_inteiro()
    layout('---', 36, f'Valor digitado {resultado}')
    continuar()

def verificar_numero_inteiro():
    if numero.is_integer():
        return int(numero)
    else:
        return float(numero)

def continuar():
    layout('---', 36, ' Continuar... ')
    escolha = str(input('>>> Você deseja continuar? (Aperte S para continuar o qualquer tecla para encerrar o programa) ')).lower()
    if escolha and escolha[0] == 's':
        os.system('cls')
        main()
    else:
        layout('===', 36, 'Programa Encerrado com Sucesso!')
        exit()

if __name__ == '__main__':
    main()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.