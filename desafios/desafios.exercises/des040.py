#colors palete
colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'red':'\033[1;31m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

#information
print('\n',' '*12,'{}In this program we calculate two types of grades:\n'.format(colors['blue']))
print('''{}Choose {}1 {}or {}2'''.format(colors['purple'],colors['green'],colors['purple'],colors['yellow']),
      '''\n\n{}1{}-Traditional grade{}(Tests with a maximum value of 10)'''.format(colors['green'],colors['gray'],colors['green']),
      '''\n\n{}2{}-Note{}(Tests with a maximum value of 100){}\n'''.format(colors['yellow'],colors['gray'],colors['yellow'],colors['clean']))
#customer interactivity
choose = (int(input('---> ')))
if choose < 1 or choose >= 3:
    print('\n{}[FAULT] Write a valid value to start the program!{}\n'.format(colors['gray'],colors['clean']))
else:
      note1 = float(input('\n{}Report your first test grade: {}'.format(colors['purple'],colors['blue'])))
      note2 = float(input('\n{}Report your second test grade: {}'.format(colors['purple'],colors['blue'])))
      print('{}'.format(colors['clean']))
      average = (note1 + note2)/2
      
      if note1 < 0 or note2 < 0:
            print('\n{}Please, write a valid value!{}\n'.format(colors['gray'],colors['clean']))
      else:
            if choose == 1:
                  if note1 >= 11 or note2 >= 11:
                        print('\n{}In this option 1, the tests have a maximum value of 10.\n\n{}Re-choose option 2!{}\n'.format(colors['gray'],colors['yellow'],colors['clean']))
                  else:
                        print('\n{}To be approved you need {}at least 6.1 points\n\n{}Your average was {}{:.2f}{}'.format(colors['gray'],colors['purple'],colors['gray'],colors['purple'],average,colors['clean']))
                        if average <= 3:
                              print('\n{}Failed student!{}\n'.format(colors['gray'],colors['clean']))
                        elif average > 3 and average <= 6.9:
                              print('\n{}Recovery student!{}\n'.format(colors['gray'],colors['clean']))
                        else:
                              print('\n{}Approved student!!\n{}'.format(colors['green'],colors['clean']))
      #Second option
            else:
                  print('\n{}In this option, your tests have a {}maximum value of 100.{}\n\nTo be approved you need {}at least 61 points!{}'.format(colors['gray'],colors['yellow'],colors['gray'],colors['purple'],colors['clean']))
                  print('\n{}Your average was {}{:.2f}{}'.format(colors['gray'],colors['purple'],average,colors['clean']))
                  if average <= 30:
                        print('\n{}Failed student!{}\n'.format(colors['gray'],colors['clean']))
                  elif average > 30 and average <= 60:
                        print('\n{}Recovery student!{}\n'.format(colors['gray'],colors['clean']))
                  else:
                        print('\n{}Approved student!!{}\n'.format(colors['green'],colors['clean']))

        
            
        
        

    