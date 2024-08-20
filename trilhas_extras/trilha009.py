import random

print('\n',' '*27,'Magic Mensage\n')

def get_answer(answer_number): #Quando a função é definida ela é ignorada até ser chamada.
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'
    
choise = random.randint(1,9) #Escolhe um número inteiro entre 1 e 9 e é armazenado em uma variável.

fortune = get_answer(choise) #A função é chamada com choise como argumento, a execução do programa segue para o inicio da função get_answer e o valor de choise é armazenado em um parâmetro chamado answer_number, então de acordo com esse valor a função retorna um de vários possiveis valores de string. A string retornada é atribuida a uma variável chamada fortune, que por sua vez é passada para uma chamada a print().

print(f'The number is {choise}!\n\n{fortune}\n')

#Sagrado Coração de Jesus eu confio em Vós. Sagrado Coração de Jesus eu espero em Ti. Amém.