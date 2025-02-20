import os

notas_da_sala = dict()

def layout(caracter, numero_multiplicador, msg):
    print()
    print(f'{caracter}'*36)
    print(' '*numero_multiplicador, f'{msg}')
    print(f'{caracter}'*36)
    print()

def verifica_numero():
    while True:
        try:
            return float(input('>>> Informe a nota para ser armazenada: '))
        except ValueError:
            layout('---', 36, '[Alert] Informe um valor numérico!')

def continuar():
    limpar_tela()
    layout('~~~', 36, ' Incluir mais valore ')
    escolha = str(input('--> would you like to continue? [s - para sim ou outra tecla para encerrar] ')).lower()
    if escolha and escolha[0] == 's':
        return True
    else:
        return False
    
def limpar_tela():
    os.system('cls')

def adicionando_valor_dicionario():
    contador = 0
    controle = True
    while controle != False:
        nota = verifica_numero()
        notas_da_sala[f'nota {contador}'] = nota
        controle = continuar()
        contador += 1

def analisando_dicionario():
    limpar_tela()
    print(notas_da_sala)


adicionando_valor_dicionario()
analisando_dicionario()
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.