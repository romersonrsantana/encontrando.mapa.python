#colors palette

#information
print('\nIn this program we calculate two types of grades:\n')
print('''Choose 1 or 2''',
      '''\n\n1-Traditional grade(Tests with a maximum value of 10)''',
      '''\n\n2-Note(Tests with a maximum value of 100)\n''')
#customer interactivity
choose = (int(input('---> ')))
if choose < 1 or choose > 3:
    print('\nWrite a valid value to start the program!\n')