#color palet
color = {'blue':'\033[1;29;44m',
         'purple':'\033[1;29;45m',
         'clean':'\033[m'}

print('\n',' '*27,'{} Desvendando os multiplos de três {}\n'.format(color['blue'],color['clean']))
print('{}'.format(color['purple']),'==='*27,'{}'.format(color['clean']),'\n')
#algoritmos
s = 0
for c in range(0,500,3):
    s = s + 500
    print(c,end=' ')
    
print('...')
print()
print('{}'.format(color['purple']),'==='*27,'{}'.format(color['clean']),'\n')
print('A somo dos valores corresponde há {}'.format(s))
    