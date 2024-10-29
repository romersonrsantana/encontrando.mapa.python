from datetime import date

print('==='*27)
print(' '*36,'Database')
print('==='*27)

worker = dict()
year_today = date.today().year

worker['name'] = str(input('>>> What is your name? '))
print()
worker['year_birth'] = int(input('>>> what is your year birth? '))
worker['year_birth'] = year_today - worker['year_birth']
print()
worker['work card'] = int(input('>>> Do you have work card? If yes... \nHow many years of membership does it have? or (--> 0 to not) '))

if worker['work card'] != 0:

    worker['work card'] = 35 - worker['work card']
    print()
    worker['wage'] = float(input('>>> What is your current or last salary? '))
    worker['years_retirement'] = worker['year_birth'] + worker['work card']

print('---'*27)
print()
print(worker)
print()
print(f'>>> Registered Name: {worker["name"]}.')
print()
print(f'>>> Age: {worker["year_birth"]} years old.')
print()
if worker['work card'] != 0:
    print(f'>>> Your retirement age will be with {worker["years_retirement"]} years old.')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.