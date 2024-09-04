print('teste')
n = int(input('Number --> '))

int = resto = resto2 = troco = resto3 = troco2 = resto4 = 0

while True:
    if n > 50:
        int = n//50
        resto = n % 50

        if n >= 100:
            print('O máximo de notas diponiveis de 50 é 100.\n\nPor favor refaça a operação!!\n')
            exit()

        elif resto == 0:
            break

        else:
            resto2 = resto//20
            troco = resto % 20
            if troco == 0:
                break
            else:
                resto3 = troco//10
                troco2 = troco % 10
                if troco2 == 0:
                    break
                else:
                    resto4 = troco2//1
                    break
    
print(f'Nota de R$ 50. --> {int}')
print(f'Nota de R$ 20. --> {resto2}')
print(f'Nota de R$ 10. --> {resto3}')
print(f'Nota de R$ 1. --> {resto4}')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.