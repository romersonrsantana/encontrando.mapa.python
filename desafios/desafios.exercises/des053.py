sentece = str(input('Digite uma frase: ')).strip().upper()
#.strip() remove todos os espaços inuteis e joga a frase para maiuscula
words = sentece.split()
#.split() separa a frase em palavras, considerando os espaços.
togther = ''.join(words)
#.join() junta todas as palavras sem espaço ou com outro caractere.
print('\nVocê digitou a frase:\n\n{}\n\n{}\n\n{}\n\n'.format(sentece, words, togther))
inverso = '' #como se fosse a variavel para o total

for letra in range(len(togther) - 1, -1, -1):
    inverso += togther[letra]

print('O inverso de {} é {}'.format(togther, inverso))

if inverso == togther:
    print('\nTemos um palíndromo!\n')
else:
    print('\nA frase digitada não é um palindromo!\n')