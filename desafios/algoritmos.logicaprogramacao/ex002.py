'''São nove moedas e entre elas há uma que é falsa. 
A moeda falsa possui um peso diferente das outras'''
#weight of coins
m1 = 6
m2 = 6
m3 = 6
m4 = 6
m5 = 6
m6 = 6
m7 = 6
m8 = 6
m9 = 6
#start of the program
print("\nAnalyzing the information of nine coins stored in the computer's memory\n")
#organizing coins
soma1 = m1 + m2 + m3
soma2 = m4 + m5 + m6
soma3 = m7 + m8 + m9
#decision structure
if soma1 == soma2 and soma1 != soma3:
    print('The counterfeit currency is in soma3\n')
    if m7 == m8:
        print('The counterfeit currency is m9 with the value of {}\n'.format(m9))
    elif m7 == m9:
        print('The counterfeit currency is m8 with the value of {}\n'.format(m8))
    else:
        print('The counterfeit currency is m9 with the value of {}\n'.format(m9))
elif soma1 == soma3 and soma1 != soma2:
    print('The counterfeit currency is in soma2\n')
    if m4 == m5:
        print('The counterfeit currency is m6 with the value of {}\n'.format(m6))
    elif m6 == m5:
        print('The counterfeit currency is m4 with the value of {}\n'.format(m4))
    else:
        print('The counterfeit currency is m5 with the value of {}\n'.format(m5))
elif soma2 == soma3 and soma2 != soma1:
    print('The counterfeit currency is in soma1\n')
    if m1 == m2:
        print('The counterfeit currency is m3 with the value of {}\n'.format(m3))
    elif m3 == m2:
        print('The counterfeit currency is m1 with the value of {}\n'.format(m1))
    else:
        print('The counterfeit currency is m2 with the value of {}\n'.format(m2))
else:
    print('All coins are not fake!!\n')
