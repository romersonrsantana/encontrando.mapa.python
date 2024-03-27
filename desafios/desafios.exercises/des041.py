from datetime import date
#colors palete

print(''' \nNational Swimming Confederation''',
      '''\nKnowing your category''','''\nBut...\n''')

currentyear = date.today().year

#User data
name = str(input('''what's, your name? '''))
print('\nNice to meet you, {}!!'.format(name))
years = int(input('\nEnter your year of birth whith four number: '))
#calculation
age = currentyear - years

#decision structure
if years > currentyear or years < 1924:
    print('\n[ERRO] Rewrite the values with the correct year!\n')
else:
      if age >= 0 and age <= 9:
            print('\n Your category is child!\n')
      elif age > 9 and age <= 14:
           print('\n Your category is children!\n')
      elif age > 14 and age <= 19:
           print('\n Your category is junior!\n')
      elif age > 19 and age <= 40:
           print('\n Your category is senior!\n')
      else:
           print('\n Your category is master!\n')