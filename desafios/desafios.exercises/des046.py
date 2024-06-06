from time import sleep
#colors palet
colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'purple-title':'\033[1;39;45m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

print(' '*27,'{} Contagem Regressiva {}'.format(colors['purple-title'],colors['clean']))
print()
for c in range(10, 0-1, -1):
    sleep(1.3)
    print()
    print(c)
    