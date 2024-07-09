print('\nIdentificando pessoas maiores de idade\n')

#primeira fase, tentar identificar se o usuário irá colocar os quatro digitos do ano conforme solicitado.
SOMA = 0
for anos_nascimento in range (7):
#Estrutura de repetição, deverão ser informados 7 anos.
    while True: 
        #estrutura de repetição para valores não iguais a 4 caracteres
        year = input('Tell me some year, *with for digits: --> ')
        quantidade = len(year)

        if int(quantidade) == 4:          
            break
        else:
            print('\nValor inválido, digite um novo valor!\n')

    SOMA = SOMA + 1
    print('\n', ' '*9, '---> Valor',SOMA,'<---')
    print('\n--> Falta informar mais {} valores para anos <--\n'.format(7 - SOMA))
try:
    int(year)
except ValueError:
    print('\n\n',' '*27,'Você digitou letras ao invés de números!!!\n O programa foi encerrado!Abra novamente o arquivo e digite valores válidos!\n')
    exit
int(year)