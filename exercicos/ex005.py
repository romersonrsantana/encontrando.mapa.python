frase = 'Curso em Video Python'
print('\n ' + frase[3] + '\n')
print(frase[0:14] + '\n')
print(frase[1:15:2] + '\n')
print(frase[::2] + '\n')
'''Tudo em pytho é um objeto'''
print(frase.count('o') , ' \n')
print(frase.upper().count('o') , ' \n')
print(len(frase.strip()) , '\n')

frase = frase.replace('Python', 'Android')
print(frase, '\n')
frase = frase.replace('Android', 'Python')
print(frase, '\n')
print(frase.find('Video'), '\n')
dividido = frase.split()
print(dividido, '\n')
print(dividido[0], '\n')
print(dividido[2][4], '\n')
