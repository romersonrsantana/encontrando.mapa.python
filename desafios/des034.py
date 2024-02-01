print('\n Bem vindo!! \n\n Projeções de Reajuste salarial\n\n')
salario = float(input('\n\n Informe o salário: '))
if salario > 36000.00:
    print('\n\n [INFORME OUTRO VALOR]. \n Considerando a folha salarial dessa empresa, não é permitido o calculo desse valor!!\n\n')
else:
    if salario <= 350.00:
        print('\n\n [ERRO]. Seu salário está muito abaixo, procure seu sindicato \n e verifique se há algo de errado!\n\n')
    else:
        if salario < 1250.00:
            print('\n\n O valor do reajuste será de 15%.\n\n O equivalente á R$ {:.2f} reais. Totalizando R$ {:.2f} reais.\n\n'.format(salario*(15/100)+salario, salario))
        else:
            if salario > 1250.00:
                print('\n\n O valor do reajuste será de 10%. \n\n O equivalente á R$ {:.2f} reais. Totalizando R$ {:.2f} reais.\n\n'.format(salario*(10/100), salario*(10/100)+salario))