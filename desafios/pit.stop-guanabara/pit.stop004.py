print('\n',' '*12 , '=-='*20)
print(' '*30 ,'Analisador de números')
print(' '*12 ,'=-='*20, '\n')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('\n Os seguimentos acimam PODEM FORMAR UM TRIÂNGULO \n!!')
else:
    print('\n Os seguimentos acima NÃO FORMAM UM TRIÂNGULO!!! \n\n')
