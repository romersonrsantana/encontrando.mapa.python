print(' \n\n ------ Avaliando a frase ------- ')
frase = str(input('\n\n Escreva uma frase: '))
print('\n\n A frase escolhida tem:\n\n {} caracteres \n\n {} letra(s) --> a \n\n Ela aparece pela primeira vez na posição --> {} \n\n' .format(len(frase),frase.upper().count('A'), frase.upper().find('A')))