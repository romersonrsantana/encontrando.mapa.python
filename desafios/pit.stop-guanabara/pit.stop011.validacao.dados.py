print('\nValidação de dados\n')

sexo = str(input('Informe seu sexo [F] para feminino ou [M] para masculino: \n\n --> ')).strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('\n\n[ALERT!] Os dados informados não correspondem a solicitação desejada! \nPor favor informe seu sexo [F] or [M]: \n\n --> ')).strip()[0]

print('\nSexo {}. Dados armazenados com sucesso!\n'.format(sexo))

#Sagrado Coração de Jesus eu confio em Vós. Sagrado Coração de Jesus eu Espero em Ti.