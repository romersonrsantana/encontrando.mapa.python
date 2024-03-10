#Paleta de cores
colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'yellow':'\033[1;33m',
          'green':'\033[1;32m',
          'red':'\033[1;31m',
          'grey':'\033[1;37m',
          'clean':'\033[m'}
#Título
print('\n',' '*20,'{}Conversor de números{}\n'.format(colors['blue'],colors['clean']))
#Informações do usuário
numb = int(input('Digite um número inteiro: '))
print('''\n{}Choose one of the options:{}\n
      {}[1]{} Converter para {}BINÁRIO{}
      {}[2]{} Converter para {}OCTAL{}
      {}[3]{} Converter para {}HEXADECIMAL{}\n'''.format(colors['grey'],colors['clean'],colors['purple'],colors['clean'],colors['purple'],colors['clean'],colors['yellow'],colors['clean'],colors['yellow'],colors['clean'],colors['green'],colors['clean'],colors['green'],colors['clean']))
choice = int(input('Sua Opção: '))
#Estrutura de DECISÃO
if choice < 0 or choice > 3:
    print('\n {}[Erro] Não há essa opção! Por favor tente novamente!{}\n'.format(colors['red'],colors['clean']))
elif choice == 1:
    print('\nO número {}{}{} convertido para {}BINÁRIO{} corresponde há {}{}{} na base(2).\n'.format(colors['purple'],numb,colors['clean'],colors['purple'],colors['clean'],colors['purple'],bin(numb)[2:],colors['clean']))
elif choice == 2:
    print('\nO número {}{}{} convertido para {}OCTAL{} corresponde há {}{}{} na base(8).\n'.format(colors['yellow'],numb,colors['clean'],colors['yellow'],colors['clean'],colors['yellow'],oct(numb)[2:],colors['clean']))
else:
    print('\nO número {}{}{} convertido para {}HEXADECIMAL{} corresponde há {}{}{} na base(16).\n'.format(colors['green'],numb,colors['clean'],colors['green'],colors['clean'],colors['green'],hex(numb)[2:],colors['clean']))


    