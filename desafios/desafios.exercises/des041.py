from datetime import date
#colors palete
colors = {'blue':'\033[1;34m',
          'clean':'\033[m',
          'grey':'\033[1;37m',
          'yellow':'\033[1;33m',
          'green':'\033[1;32m',
          'lightgreen':'\033[1;36m',
          'purple':'\033[1;35m',}

print('\n',' '*21,'''{}National Swimming Confederation{}'''.format(colors['blue'],colors['clean']),
      '''\n\n{}Knowing your category'''.format(colors['grey']),'''\nBut...\n''')

currentyear = date.today().year

#User data
name = str(input('''{}what's, your name?{} '''.format(colors['purple'],colors['blue'])).upper())
print('\n{}Nice to meet you, {}!!'.format(colors['grey'],name))
years = int(input('\n{}Enter your year of birth whith four number:{} '.format(colors['purple'],colors['blue'])))
#calculation
age = currentyear - years

#decision structure
if years > currentyear or years < 1924:
    print('\n{}[ERRO]{} Rewrite the values with the correct year!{}\n'.format(colors['yellow'],colors['grey'],colors['clean']))
else:
      if age >= 0 and age <= 9:
            print('\n {}Your category is child!{}\n'.format(colors['grey'],colors['clean']))
      elif age > 9 and age <= 14:
           print('\n {}Your category is children!{}\n'.format(colors['yellow'],colors['clean']))
      elif age > 14 and age <= 19:
           print('\n {}Your category is junior!{}\n'.format(colors['lightgreen'],colors['clean']))
      elif age > 19 and age <= 40:
           print('\n {}Your category is senior!{}\n'.format(colors['purple'],colors['clean']))
      else:
           print('\n{}Your category is master!{}\n'.format(colors['blue'],colors['clean']))