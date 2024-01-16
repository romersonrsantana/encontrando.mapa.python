print('\n Bem vindo ao analiazador de nomes!! \n')
nome = str(input(' Digite seu nome completo: '))
junto = nome.split()
print('\n Olá {}!! \n Seu nome em letras maiusculas é {} \n Seu nome em letras minusculas {} \n Seu nome e sobrenome somados tem {} letras \n Seu primeiro nome {} letras \n\n Obrigado por usar nosso programa {}!! \n\n'.format(nome, nome.upper(), nome.lower(), len(''.join(junto)), len(junto[0]), junto[0]))