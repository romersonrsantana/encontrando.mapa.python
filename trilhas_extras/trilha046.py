import re

phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Informamos o padrão desejado e armazenamos o objeto regex resultante em phone.

user = str(input('Enter a phone number: (xxx-xxx-xxxx) >>> '))

tes = phone.search(user)

print()
if tes == None:
    print("You didn't provide a phone number!")
else:
    print(f'Your phone number provide is: {tes.group()}')
print()

#print('>>> Phone number is ', phone.search(user).group()) #Em seguida foi passado search em phone e foi informado a string que queremos encontrar uma correspondência

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.