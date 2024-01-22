print(' \n\n ------ Avaliando a frase ------- ')
frase = str(input('\n\n Escreva uma frase: ')).upper()
print('\n\n A frase escolhida tem:\n\n {} caracteres \n\n {} letra(s) --> a \n\n Ela aparece pela primeira vez na posição --> {} \n\n A última letra aparece {}' .format(len(frase),frase.upper().count('A'), frase.find('A')+1, frase.rfind('A')+1))