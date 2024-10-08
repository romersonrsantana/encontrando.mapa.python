print('==='*27)
print(' '*27,'Distinct Groups')
print('==='*27)

even = list() #par
odd = list() #impar
total = list()

for c in range(1, 7):

    number = (int(input('--> Enter an integer: ')))
    print()

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

total.append(even[:])
even.clear()
total.append(odd[:])
odd.clear()
total[0].sort()
total[1].sort()

print('---'*27)
print(f'>>> The numbers odd are: {total[1]}.')
print(f'>>> The numbers even are: {total[0]}.')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.