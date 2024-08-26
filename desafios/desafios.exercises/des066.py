print('\n', ' '*27,'Somando números inteiros\n')

total = 0
loop_sum = 0

while True:

    number = int(input('\nEnter a number or enter 999 to end the program:\n\n--> '))

    if number == 999:
        break

    total += number

    loop_sum += 1

print(f'\nThe sum of the numbers is {total}.\n\nReported quantity {loop_sum}.\n')

