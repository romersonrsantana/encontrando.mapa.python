print('\n',' '*27,'Somando inteiros\n')

condicao_parada = 0
contador = 0
total = 0

print('\nInforme números para serem somados ao final da sequência ou digite (999) para encerrar:\n')

while condicao_parada != 999:

    condicao_parada = int(input('\n--> '))

    if condicao_parada == 999:
        print('\nPrograma finalizado com sucesso!!\n')

    else:
        contador += 1
        total += condicao_parada

print(f'\nForam somados: --> {contador} números! \n\nTotal da soma --> {total}\n\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moíses. Toda Honra e Toda Glória Ao Espirito Santo. Toda Honra e Toda Glória Ao Nosso Senhor Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.