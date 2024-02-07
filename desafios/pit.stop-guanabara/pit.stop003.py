print('\n\n','='*20, 'Menor e Maior valor', 20 *'=')
n1 = float(input('\n\n Digite o primeiro valor: '))
n2 = float(input('\n\n Digite o segundo valor: '))
n3 = float(input('\n\n Digite o terceiro valor: '))

#Verificando o menor valor
menor = n1
if n2 < n1 and n2 < n3:
   menor = n2
if n3 < n1 and n3 < n2:
   menor = n3
#Verificano o maior valor
maior = n3
if n3 < n1 and n2 < n1:
   maior = n1
if n1 < n2 and n3 < n2:
   maior = n2
print('\n','=-='*6, 'O menor valor é {}'.format(menor),'=-='*6)
print('\n','=-='*6,'O maior valor é {}'.format(maior),'=-='*6,'\n\n')
