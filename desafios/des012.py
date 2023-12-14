mensagem = str('Calculo de desconto')
print('\n\n {:-^63} \n\n' .format(mensagem))

precoproduto = float(input('Digite o valor do produto para o desconto: '))

descontoporcento = float(input('Insira quanto de desconto você deseja aplicar \n (valores permitidos de 1 a 100%): '))

desconto = (precoproduto * (descontoporcento / 100))
valorfinal = (precoproduto - desconto)

print('O valor informado para o desconto foi de R$ {} o desconto será de {} %. \n\n Caro cliente o desconto será de R$ {} reais. \n Seu produto sairá por R$ {} reais' .format(precoproduto, descontoporcento, desconto, valorfinal ))