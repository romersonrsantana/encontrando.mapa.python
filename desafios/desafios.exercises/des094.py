print('---'*27)
print(' '*36, 'Data history')
print('---'*27)

person = dict()
woman = list()
up_age = list()
people_list = list()
total = control = 0

def layout(dicionary):
    for c in dicionary:
        for k, v in c.items():
            if k == 'name':
                print(f'{v}... ', end='')

while True:
    print()
    person[f'name'] = str(input('>>> Enter a Name: '))
    print()
    person[f'sexo'] = str(input('>>> Write the sexo (M - masculino or F - feminino) '))[0].lower()
    print()
    person[f'age'] = int(input(f">>> Enter the {person[f'name']}'s age "))
    print()

    people_list.append(person.copy())
    person.clear()

    choise = str(input('>>> Do you to continue? (y - yes or n - not) ')).lower()[0]
    print()

    if choise == 'n':
        break
# ---------------- Identifying Women -------------------- 
for c in people_list:
    for k, v in c.items():
        if v == 'f' or v == 'feminino':
            woman.append(c.copy())

# --------------- Average Age -------------------------- 
        if k == 'age':
            total += v
            control += 1

# -------------- Above average Age ---------------------
for c in people_list:
    for k, v in c.items(): 
        if k == 'age' and v > total/control:
            up_age.append(c.copy())

print('==='*27)
print(f'  >>> Total number of registered people: -- {len(people_list)} --.')
print()
print(f'  >>> The average age of the group: -- {total/control:.2f} --.')
print()
print(f'  >>> Registered Women:   ', end='')
layout(woman)
print()
print()
print(f'  >>> People above average age:   ', end='')
layout(up_age)
print()
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.