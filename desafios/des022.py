print('\n Bem vindo ao analiazador de nomes!! \n')
nome = str(input(' Digite seu nome completo: '))
print('\n Olá {}!! \n Seu nome em letras maiusculas é {} \n Seu nome em letras minusculas {} \n Seu nome e sobrenome tem {} letras '.format(nome, nome.upper(), nome.lower(), nome.split().len(nome)))