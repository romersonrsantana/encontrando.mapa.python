from datetime import date
ano_atual = date.today().year

#palet_color
color = {'blue':'',
         'purple':'',
         'yellow':'',
         'green':'',
         'gray':'',
         'alert':'',
         'clean':''}

print(' '*27,'\nIdentificando anos correspondentes a pessoas menores de idade.\n Os anos informados acima do ano atual de {}, serão desconsiderados.'.format(ano_atual))

#primeira fase, tentar identificar se o usuário irá colocar os quatro digitos do ano conforme solicitado.

#variáveis globais para controle.
SOMA = 0
MENOR_IDADE = 0
FORA_DO_PADRAO = 0
TODAS_IDADES = 0

for anos_nascimento in range (7):
#Estrutura de repetição, deverão ser informados 7x anos aleatórios.
    while True: 
        #estrutura de repetição para valores não iguais a 4 caracteres
        year = input('\n\nTell me some year, *with for digits: --> ')
        quantidade = len(year)

        if int(quantidade) == 4:          
            break
        else:
            print('\nValor inválido, digite um novo valor!\n')

    #Dados de saída. O laço SOMA indica na tela para o usuário quantas vezes o mesmo já digitou o valor solicitado e quantos ainda falta. 
    SOMA = SOMA + 1
    print('\n', ' '*9, '---> Valor',SOMA,'<---')
    print('\n--> Falta informar mais {} valores para anos <--\n'.format(7 - SOMA))

    #Dados de Saída. Mensagem de erro caso o usuário tenha digitado letras.
    try:
        int(year)
    except ValueError:
        print('\n',' '*18,'Você digitou outros caracteres ao invés de números!!!\n',' '*18,'O valor informado não será considerado!\n')
        continue
    convercao = int(year)
    
    #Depois de converter a string para int, será classificado os anos, ref.: acima ou abaixo de 18 anos.
    if ano_atual - convercao < 18 and ano_atual - convercao >= 0:
        MENOR_IDADE += 1
    elif ano_atual < convercao:
        FORA_DO_PADRAO += 1
    elif ano_atual - convercao > -1:
        TODAS_IDADES += 1

#Dados de saída para o usuário com os resultados.

print('Estamos em -->',ano_atual,'\n')
print('\nDos anos informados:\n--> {} abaixo de --> 18 anos\n'.format(MENOR_IDADE))
print('\n--> {} Fora da lógica. Ano de nascimento superior ao ano atual.\n'.format(FORA_DO_PADRAO))
print('\n--> {} Válido(s) para Idades livres apartir de 18 anos\n'.format(TODAS_IDADES))
