import os

def layout( caracter, numero_multiplicador, msg):
    print(f'{caracter}'*36)
    print(' '*numero_multiplicador, f'{msg}')
    print(f'{caracter}'*36)

def limpar():
    os.system('cls')

def usuario():
    while True:
        try:
            return int(input('>>> Informe um número: '))
        except ValueError:
            limpar()
            layout('---', 9, '[Alert] Informe um valor númerico!')

def loop(valor_1, valor_2, passo=1):
    for c in range(valor_1, valor_2, passo):
        print(f'... {c} ', end='')
    print()

def continuar():
    layout('---', 36, 'Continuar')
    resposta = str(input(' >>> Você quer continuar? (Aperte S para sim ou qualquer tecla para concluir) ')).lower()
    if resposta and resposta[0] == 's':
        limpar()
        main()
    else:
        layout('===', 36, 'Programa Encerrado com Sucesso!')
        exit()

def main():
    layout('===', 36, ' Contagem Crescente ou Decrescente ')
    inicio = usuario()
    objetivo = usuario()
    if inicio < objetivo:
        loop(inicio, objetivo + 1, passo = 1)
    else:
        loop(inicio, objetivo - 1, passo = -1)
    continuar()

if __name__ == '__main__':
    main()
    continuar()
    
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Isarel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.