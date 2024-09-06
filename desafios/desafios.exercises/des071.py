print('==='*18)
print(' '*27,'Atm')
print('==='*18)
print('\n\n','---'*7 + ' Sake ' + '---'*7)

inteiro = resto = resto2 = troco = resto3 = troco2 = resto4 = 0
boolean = False

while boolean != True:
    sake = int(input('\nWhat amount do you want to withdraw?\n\n--> U$ '))

    while True:
        if sake > 50:
            inteiro = sake//50
            resto = sake % 50

            if inteiro >= 100:
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
    print('---'*7 + ' Quantity of banknotes for whithdrawal ' + '---'*7)
    print(f'\nNota de R$ 50,00 --> {inteiro}.')
    print(f'Nota de R$ 20,00 --> {resto2}.')
    print(f'Nota de R$ 10,00 --> {resto3}.')
    print(f'Nota de R$ 1,00 --> {resto4}.\n')
    print('---'*27)

    while True:
        choice = str(input('\nDo you want to make any more withdrawals?[y] yes or [N] not \n\n--> ')).strip().lower()

        if choice == 'y':
            break
        elif choice == 'n':
            boolean = True
            break
        else:
            print("\n[Alert!] Choose [Y] for 'yes' or [N] to 'not'.\n")
print('\n'+'==='*27)
print(' '*27,'Program ended successfully')
print('==='*27+'\n')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés. Toda Honra e Toda Glória Ao Espiríto Santo. Toda Honra e Toda Glória A Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.