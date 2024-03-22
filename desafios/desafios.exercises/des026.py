print(' \n\n ------ Avaliando a frase ------- ')
frase = str(input('\n\n Escreva uma frase: ')).upper().strip()
print('\n\n A frase escolhida tem:\n\n {} caracteres \n\n {} letra(s) --> a \n\n Ela aparece pela primeira vez na posição --> {} \n\n A última letra aparece {}' .format(len(frase),frase.upper().count('A'), frase.find('A'), frase.rfind('A')))
print('\n\n A escala considerada começa em 0 \n\n')