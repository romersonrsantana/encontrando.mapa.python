numero = int(input('Digite um número: '))
antece = numero - 1
suces = numero + 1

print('O número escolhido foi {:=^ 20} , \n seu antecessor {:-> 20} , \n seu sucessor {:-> 20} '.format(numero, antece, suces))