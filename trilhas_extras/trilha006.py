import sys

while True:
    print('Type exit to exit.')
    response = str(input())

    if response == 'exit':
        sys.exit()
    print('You typed' + response + '.')