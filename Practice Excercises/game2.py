import random
import sys

board = [i for i in range(0, 9)]


def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = '\n'
            if x != 1:
                end += '----------\n'
        char = ' '
        if i in ('X', 'O'):
            char = i
        x += 1
        print(char, end=end)


def select_player():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def moves_available():
    return board.count('X') + board.count('O') != 9

# Begin application loading rules


player, computer = select_player()
result = "DRAW"

print('Welcome to my Tic Tac Toe Game.\n')
print(f"After a coin toss, AI plays as {computer} and Human plays as {player}. X Plays first.")

while moves_available():
    print_board()
    while True:
        try:
            move = int(input('Choose where to play [1 - 9]: '))
        except ValueError:
            print('Please enter a valid number from 1 to 9.')
            continue
        else:
            break