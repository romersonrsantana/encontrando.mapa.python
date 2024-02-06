from datetime import date
nome = str(input('\n\n Digite seu nome para iniciar: ')).upper()
print('\n\n Seja Bem Vindo(a) {}!! \n\n Aqui vamos descobrir todos os anos bissextos que desejar!! \n\n'.format(nome))
ano = int(input('Informe um ano válido: '))
if ano == 0:
    ano = date.today().year
if ano < 1582:
    print('\n\n [ERRO!!] O ano informado não é valido!!\n\n Considerando o cal1endário gregoriano o ano mínimo permitido é 1582, quando passou a vigorar. \n\n')
else:
    if (ano% 4) == 0 and (ano%100) != 0 or ano % 400 == 0:
        print('\n\n O ano informado é BISSEXTO!! \n\n Nele {}, você terá um dia a mais para lutar pelos seus sonhos!!\n\n Louvado Seja Nosso Senhor Jesus Cristo.\n Para Sempre Seja Louvado. Amém.\n\n'.format(nome))
    else:
        print('\n\n Não. {} NÃO É UM ANO BISSEXTO!! \n\n'.format(ano))