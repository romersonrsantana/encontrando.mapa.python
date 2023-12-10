#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:20} !'.format(nome))
#print('Prazer em te conhecer {:>20} !' .format(nome))
#print('Prazer em te conhecer {:^20} !' .format(nome))
#print('Prazer em te conhecer {:=^20} !' .format(nome))
#print('Prazer em te conhecer {:=>20} !' .format(nome))
n1 = int(input('Digite um número :'))
n2 = int(input('Digite um outro número: '))
s = n1 + n2
sub = n1 - n2
restv = n1%n2
m = n1 * n2
d = n1/n2
di = n1 // n2

print('Os resultado das contas envolvendo {} e {} são: ' .format(n1, n2), end = '')
print('Soma {}, subtração {}, produto {}, divisão {:.3f}, divisão inteira {}, resto {}' .format(s, sub, m, d, di, restv))