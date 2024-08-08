
controle = 0

n = int(input('--> '))
pa = int(input('--> '))

while controle < 10:
    controle += 1

    if controle == 1:
        total = n
        print(total)

    else:
        total += pa
        print(total)