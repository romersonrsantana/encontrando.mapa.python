while True:
    month = int(input('\n' + ' '*27 + '########### Menu ########## \n\nInforme um número válido de 1 ao 12 para indicarmos seu respectivo mês: ---> '))  
    if month >= 1 and month <= 12:
        break

months_dict = {1 : 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
7: 'July', 8: 'August', 9: 'September', 10: 'Octuber', 11: 'November', 12: 'December'
}

print('\nO mês escolhido foi ' + months_dict[month] + '\n')