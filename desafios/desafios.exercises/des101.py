from datetime import date

def layout(caractere, msg):
    print(f'{caractere}' * 36)
    print(' '*36,f'{msg}')
    print(f'{caractere}' * 36)


def vote(year_of_birth):
    years_old = current_year - year_of_birth

    if years_old >= 0 and years_old < 16:
        return f"You are {years_old} years old.Vote denied."
    elif years_old == 16 or years_old == 17 or years_old > 70 and years_old < 112:
        return f"You are {years_old} years old. Opitional vote."
    elif years_old >= 18 and years_old < 70:
        return f"You are {years_old} years old. Mandatory vote."

current_year = date.today().year

layout('===', 'Right to vote')

while True:
    user = int(input('>>> Enter your year of birth --> '))

    if user > current_year:
        print('[ERRO] Year not accepted')
    elif user <= current_year and user > 1913:
        break
    else:
        print('[ERRO] Year not accepted, vampire!')

response = vote(user)
print()
print(f'        >>> As for your vote this year, {response} ')
print()

#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Ao Seu Único Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.