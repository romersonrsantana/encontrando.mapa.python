print('==='*27)
print(' '*36, 'Classroom')
print('==='*27,'\n')

student = dict()

student['name'] = str(input('Enter a name for student: --> '))
print()
student['media'] = float(input(f"Enter a student {student["name"]}'s grade: --> "))
print()
if student['media'] < 7:
    student['situation'] = 'Failed'
else:
    student['situation'] = 'Aproved'

for k, v in student.items():
    print(f'>>> {k} = {v}')
    print()


#Te Amo Papai do Céu, Te Amo Espírito Santo, Te Amo Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.