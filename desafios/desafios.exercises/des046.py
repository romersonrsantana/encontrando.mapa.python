import emoji
from time import sleep
#colors palete
colors = {'blue':'\033[1;39;44m',
          'purple':'\033[1;39;45m',
          'gray':'\033[1;37m',
          'clean':'\033[m'}

print(' '*27,'{} Contagem Regressiva {}'.format(colors['purple'],colors['clean']))
print()
sleep(1.6)
print(' '*27,'{}       Ready...  🧨  {}'.format(colors['blue'],colors['clean']))
for c in range(10, 0-1, -1):
    sleep(1.3)
    print()
    print('{}--->{} '.format(colors['gray'],colors['clean']),c)
    sleep(1.6)
print()
print(emoji.emojize("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥💥💥\n"))