import emoji
print('\nTabuada com estrutura de repetição\n')

while True:
    number = int(input('Insira um número inteiro entre 0 e 10: '))
    if number >= 0 and number < 11:  
        break
print()
print(emoji.emojize("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪"*2))
print()

for c in range(0, 11):
    print(' '*27,'{} x {} = {}'.format( number, c, number*c))

print()
print(emoji.emojize("🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪"*2))
    
    
   
