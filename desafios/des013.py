titulo = 'Reajuste salarial'
cumprimento = 'Bem vindo(a)!!'
mensagem = 'Siga as orientações abaixo para um melhor aproveitamento do programa'

print('\n\n{:-^63} \n\n {:^63} \n\n {} \n\n' .format(titulo, cumprimento, mensagem))
salario = float(input('Digite seu salário atual: '))
taxareajuste = float(input('\n\nEscolha quantos porcento será reajustado: '))
novosalario = salario + (salario*(taxareajuste/100))

print('\n\nCom um reajuste de {:.2f}%. Seu salário que era R${:.2f}, agora é R${:.2f}. \n\n Seu reajuste foi de R${:.2f} \n\n' .format(taxareajuste, salario, novosalario, (novosalario - salario)))