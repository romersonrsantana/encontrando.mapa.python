import random
print('\n\n ------ Adivinhando um número --------')
numb = int(input('\n\n Escolha um número de 0 a 5: '))
if numb < 0 or numb > 5:
    print('\n\n O número escolhido não é válido!')
seqNum = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(seqNum)
print('\n\n Seu palpite foi o número {} '.format(numb))
if numb == escolhido:
    print('\n\n PARABÉNS você acertou o número escolhido pelo computador \n\n!!!')
else:
    print('\n\n ERROU!! O número escolhido pelo computador foi  {:=^20}  \n\n'.format(escolhido))