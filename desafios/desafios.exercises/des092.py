from datetime import date
print('==='*27)
print(' '*36,'Database')
print('==='*27)

worker = dict()
year_today = date.today().year

worker['name'] = str(input('>>> What is your name? '))

worker['year_birth'] = int(input('>>> what is your year birth? '))
worker['year_birth'] = year_today - worker['year_birth']

worker['work card'] = int(input('>>> Do you have work card? If yes... How many years of membership does it have? or (--> 0 to not) '))

if worker['work card'] != 0:
    
    worker['year_of_hire'] = int(input('>>> What was the year of your last hire? '))

    worker['wage'] = float(input('What is your current salary or your last salary? '))

print(worker)
#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.