def layout(caracter, msg):
    print(f'{caracter}'*36)
    print(' '*36, f'{msg}')
    print(f'{caracter}'*36)


def record(name = 0, goals_total = 0):
    if name != 0 or goals_total != 0:
        for k, v in football_players.items():
            if name == k or goals_total == v:
                print(f'>>> Name: {k} : {v} goals.')
    else:
        print()
        print('     [Alert] Informe os dados...')
        print()

def name():
    return str(input('>>> Enter a name player: '))


def goals():
    while True:
        try:
            return int(input('>>> Enter a goals numbers: '))
        except ValueError:
            print('\n [Error] Enter an integer. ')
            print()


football_players = {'João': 26 , 'Tereza': 27 }


def main():
    layout('===', 'Checker')
    record(name(), goals())


if __name__ == '__main__':
    main()


#Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés E Toda Honra e Toda Glória Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.