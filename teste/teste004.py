from time import sleep
#colors palet
colors = {'blue':'\033[1;34m',
          'purple':'\033[1;35m',
          'green':'\033[1;32m',
          'yellow':'\033[1;33m',
          'clean':'\033[m'}
print(' '*27,'{} Countdown - Test {}'.format(colors['blue'],colors['clean']))

lista = ('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')

print('{}Ready... 🧨{}'.format(colors['yellow'],colors['clean']))
sleep(1.2)
print(' '*27,'{} Go 💨💨💨💨 {}'.format(colors['green'],colors['clean']))
print()
sleep(1.2) 

for c in range(10, 0-1, -1):
    print('{}---> {}'.format(colors['purple'],colors['clean']),lista[c])
    sleep(1.2)
    print()
print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
print()


    

