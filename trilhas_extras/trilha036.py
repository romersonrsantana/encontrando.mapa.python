print('==='*27)
print(' '*36,'Tic Tac Toe')
print('==='*27)

the_board = {'top-left':'', 'top-center':'', 'top-right':'',
             'mid-left':'', 'mid-center':'', 'mid-right':'',
             'low-left':'', 'low-center':'', 'low-right':''}

def Board(board):
    print()
    print(board['top-left'] + '|' + board['top-center'] + '|' + board['top-right'])
    print('---'*9)
    print(board['mid-left'] + '|' + board['mid-center'] + '|' + board['mid-right'])
    print('---'*9)
    print(board['low-left'] + '|' + board['low-center'] + '|' + board['low-right'])
    print()

turn = 'x'

for i in range(9):
    Board(the_board)
    print(f'Turn for {turn:-^9}. Write the place to move on which space... ')
    move = input('''
                 
    top-left | top-center | top-right
----------------------------------------           
    mid-left | mid-center | mid-right
----------------------------------------
    low-left | low-center | low-right
        
    ---> ''')
    the_board[move] = turn

    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    
    Board(the_board)

#Eis-me Aqui... Estou disponível só pra Te Servir. Eu não quero dizer não para o Seu Chamado... Toda Honra e Toda Glória Ao Deus de Abraão, Isaac, Jacó, Israel e Moisés e Ao Seu Filho Amado Jesus Cristo. Louvado Seja Nosso Senhor Jesus Cristo. Para Sempre Seja Louvado. Amém.