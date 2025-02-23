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
        notas_da_sala[f'nota {contador + 1}'] = nota
        controle = continuar()
        contador += 1

def bigger():
    maior = 0
    for k, v in notas_da_sala.items():
        if k == 'nota 1':
            maior = v
        else:
            if maior < v:
                maior = v
    return maior

def smaller():
    menor = 0
    for k, v in notas_da_sala.items():
        if k == 'nota 1':
            menor = v
        else:
            if v < menor:
                menor = v
    return menor

def analisando_dicionario():
    limpar_tela()
    quantidade_de_notas = len(notas_da_sala)
    layout('---', 36, f'--> Foram cadastradas {quantidade_de_notas} notas!')
    maior_nota = bigger()
    layout('===', 36, f'--> A maior nota foi {maior_nota}!')
    menor_nota = smaller()
    layout('---', 36, f'--> A menor nota foi {menor_nota}!')




adicionando_valor_dicionario()
analisando_dicionario()
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.