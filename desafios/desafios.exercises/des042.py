#colors palette
print('\nCondition for the existence of a triangle\n\nEnter 3 values for 3 lines and find out if these lines can form a triangle!\n')
#user data
line1 = float(input('\n\n Straight1 ---> '))
line2 = float(input('\n\n Straight2 ---> '))
line3 = float(input('\n\n Straight3 ---> '))
#condition
if(line1 + line2) > line3 and (line1 + line3) > line2 and (line2 + line3) > line1:
    print('\n\nwith these stright lines, It is possible to form triangle!!\n')
    if line1 == line2 == line3:
        print('\nThis is an equilateral:\n')
    elif line1 == line2 != line3:
        print('\nThis is an isoceles triangle:')
    elif line1 == line3 != line2:
        print('\nThis is an Isosceles triangle:')
    elif line2 == line3 != line1:
        print('This is an Isoceles trinangle \n\n')
    elif line2 != line3 != line2:
        print('\nThis is scalene!', '\n\nAll sides are different!\n\n\n')
else:
    print('\nIt is not possible to form a triangle\n')
