#color palet
color = {'blue':'\033[1;29;44m',
         'purple':'\033[1;29;45m',
         'clean':'\033[m'}

print('\n',' '*27,'{} Desvendando os multiplos de três {}\n'.format(color['blue'],color['clean']))
print('{}'.format(color['purple']),'==='*27,'{}'.format(color['clean']),'\n')
#algoritmos
s = 0
for c in range(3,501,3): #lógica errada porque multiplos são aqueles que o resto da divisão é zero. E não apenas pular de 3 em 3.
    s = s + 501
    print(c,end=' ')
    
print('...')
print()
print('{}'.format(color['purple']),'==='*27,'{}'.format(color['clean']),'\n')
print('A soma dos valores corresponde há {}'.format(s))
    