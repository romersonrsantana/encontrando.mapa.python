#color palette
colors = {'blue':'\033[7;34m',
          'text':'\033[1,34m',
         'whitegreen':'\033[1;36;47m',
         'yellow':'\033[7;1;43m',
         'limpa':'\033[m'}
#title
print('\n\n {}  Welcome to the names selector!!  {}\n\n'.format(colors['whitegreen'],colors['limpa']))
name = str(input(' {}   Provide your name: {} '.format(colors['blue'], colors['limpa']))).upper()
if name == 'JOÃO'or name == 'JOAO' or name == 'TEREZA':
    print('\n {} You have a beautiful name! {}'.format(colors['text'],colors['limpa']))
elif name in 'MARIA PAULA ROBERTO JORGE PEDRO FRANCISCA JOANA JOSEFA':
    print('\n Your name is very popular in Brazil!')
else:
    print("\n I don't have any updates on your name.")
print('\n {} Have a nice Day, {}!!! {} \n\n'.format(colors['yellow'],name,colors['limpa']))