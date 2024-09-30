print('==='*27)
print(' '*27, 'tic tac toe')
print('==='*27)

the_board = {'top_left':'', 'top_mid':'', 'top_right':'',
             'mid_left':'', 'mid_mid':'', 'mid_right':'',
             'low_left':'', 'low_mid':'', 'low_right':''} #estrutura de dados

def print_board(board):
    print(board['top_left'] + '|' + board['top_mid'] + '|' + board['top_right'])
    print('-+-+-')
    print(board['mid_left'] + '|' + board['mid_mid'] + '|' + board['mid_right'])
    print('-+-+-+')
    print(board['low_left'] + '|' + board['low_mid'] + '|' + board['low_right'])    #Como criamos uma estrutura de dados para representar um tabuleiro de jogo da velha e implementamos o código em print_board para interpretar essa estrutura de dados, tenho agora um programa que "modela" o tabuleiro de jogo da velha.

    print('\n'*3)

print_board(the_board) #Exibe um tabuleiro vazio

the_board['top_left'] = 'O'

print_board(the_board)

#Minha vida só faz sentido quando o Senhor Deus de Abraão, Isaac, Jacó e Israel e Seu Filho Amado Jesus estão diante de mim. Louvado Seja Nosso Senhor Jesus Cristo, Para Sempre Seja Louvado. Amém.