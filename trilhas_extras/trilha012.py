print(' '*27,'\nTeste!\n')

def spam():
    eggs = '\nspam local\n'
    print(eggs)    #escopo local
    
                        #Há três variáveis nesse programa,

def bacon():
    eggs = '\nbacon local\n'
    print(eggs)         #escopo local
    spam()
    print(eggs)

eggs = '\nglobal\n'
bacon()
print(eggs)             #escopo global

#Sagrado Coração de Jesus, confio e espero em Vós. Amém.