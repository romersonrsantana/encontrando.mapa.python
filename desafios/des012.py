mensagem = str('Calculo de desconto')
print('\n\n {:-^63} \n\n' .format(mensagem))

precoproduto = float(input('Digite o valor do produto para o desconto: '))

descontoporcento = int(input('\n\n Insira quanto de desconto você deseja aplicar \n\n (valores permitidos de 1 a 100%): '))

desconto = (precoproduto * (descontoporcento / 100))
valorfinal = (precoproduto - desconto)

print('\n\n O valor informado para o desconto foi de R$ {:.2f} o desconto será de {}%. \n\n Caro cliente o desconto será de R$ {:.2f} reais. \n\n Seu produto sairá por R$ {:.2f} reais \n\n' .format(precoproduto, descontoporcento, desconto, valorfinal ))