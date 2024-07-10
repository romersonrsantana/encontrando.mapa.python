print('\n',' '*27,'Identificando pesos\n')

people = []
for kg in range (1,6):
    while True:
        try:
            peso = (float(input('\nInforme o {}ª peso humano: --> '.format(kg))))    
        except ValueError:
            print('\n',' '*9,f'[ERRO] Você digitou outros tipos de caracteres que não correspondem a números!\n',' '*9, '[ALERT] O valor passado não será considerado!!\n')
            continue   
        if peso > 1 and peso <= 595:
            break
        elif peso > 595:
            print('\n[ERRO] Informe um valor válido, o maior peso que se te registro \né do Mexicano Juan Pedro Franco com 595KG.')
        elif peso < 0.45:
            print('\n[ERRO] O valor minimo considerado é de recém nascidos com até 450G\n')
    
    people.append(peso)
maior_peso = max(people)
menor_peso = min(people)

print(f'\n\nOs pesos são: --> {people}\n\n---> O maior peso será: {maior_peso}\n\n---> O menor peso será: {menor_peso}\n')
#Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.