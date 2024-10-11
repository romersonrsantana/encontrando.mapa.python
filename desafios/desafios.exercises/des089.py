print('==='*27)
print(' '*36,'Database')
print('==='*27)

average_students = list()
student = list()
control = 1

#----------------- Questionary ----------------------
while True:
    print()
    student.append(str(input(f"Enter the name of the {control}st student: ")))
    student.append(float(input(f'Enter the first note: ')))
    student.append(float(input(f'Enter a second nota: ')))
    student.append(float((student[1] + student[2]) / 2))
    print('---'*27)
    average_students.append(student[:])
    student.clear()

    control += 1

#------------------- STOP OPTION TO ENTER NEW STUDENTS ------

    choise = str(input('Do you want to continue? [y - yes or n - not] >>> ')).lower()[0]

    if choise == 'n':
        break

    print('==='*27)
    print()

#--------------------------- RESULT -------------------------
for c, value in enumerate(average_students):
    print()
    print(f'-- {value[0]}. Média: --> {value[3]:.2f}')

#----------------- OPTION TO COMPLETE THE PROGRAM -----------
while True:
    print()
    choise = str(input(">>> Would you like to see a specific student's grade? [y - yes or n - not] ")).lower()[0]

    if choise == 'n':
        print()
        print(' '*36,'Program completed!\n')
        break

#---------------- INDEX FOR STUDENT INFORMATION -------------
    print()
    for indice, name in enumerate(average_students):

        print(f'--> [{indice:^9}] - {name[0]}.')

#--------- INDIVIDUAL PRESENTATION OF THE CHOSEN STUDENT ----
    print()

    choise = int(input('Enter the corresponding student number: --> '))
    print()

    for c, v in enumerate(average_students[choise]):

        if c == 3:
            print(f' Média: {v:.2f}.')
        else:
            print(f'>>> Nota: {v}... ', end='')

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.