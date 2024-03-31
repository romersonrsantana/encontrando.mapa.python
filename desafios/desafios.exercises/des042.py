#colors palette
colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'blupur':'\033[1;34;45m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'ligthgreen':'\033[1;36m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}
print('\n{}  Condition for the existence of a triangle  {}\n\n{}Enter {}3 values{} for {}3 lines{} and find out if these lines{} can form a triangle!{}\n'.format(colors['blupur'],colors['clean'],colors['blue'],colors['purple'],colors['blue'],colors['purple'],colors['blue'],colors['purple'],colors['clean']))
#user data
line1 = float(input('\n\n {}Straight1 --->{} '.format(colors['gray'],colors['green'])))
line2 = float(input('\n\n {}Straight2 --->{} '.format(colors['gray'],colors['green'])))
line3 = float(input('\n\n {}Straight3 --->{} '.format(colors['gray'],colors['green'])))
#condition
if(line1 + line2) > line3 and (line1 + line3) > line2 and (line2 + line3) > line1:
    print('\n\n{}with these stright lines, It is possible to form triangle!!{}\n'.format(colors['yellow'],colors['clean']))
    if line1 == line2 == line3:
        print('\n{}This is an {}equilateral:{}\n'.format(colors['gray'],colors['ligthgreen'],colors['clean']))
    elif line1 == line2 != line3:
        print('\n{}This is an {}isoceles triangle!{}'.format(colors['gray'],colors['ligthgreen'],colors['clean']))
    elif line1 == line3 != line2:
        print('\n{}This is an{} Isosceles triangle! {}'.format(colors['gray'],colors['ligthgreen'],colors['clean']))
    elif line2 == line3 != line1:
        print('{}This is an{} Isoceles trinangle!{}\n\n'.format(colors['gray'],colors['ligthgreen'],colors['clean']))
    elif line2 != line3 != line2:
        print('\n{}This is{} scalene!{}'.format(colors['gray'],colors['ligthgreen'],colors['gray']), '\n\nAll sides are different!{}\n\n\n'.format(colors['clean']))
else:
    print('\n{} [ERRO] {}It is not possible to form a triangle!! {}\n'.format(colors['yellow'],colors['gray'],colors['clean']))
