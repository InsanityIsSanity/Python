import os

# Set global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = ['','X']
winner = ''
won = 0
draw = 0
game_in_progress = 0
winning_blocks = ''

def start_game():
    # load decision function for who plays first
    master_slave()

def master_slave():
    # decide who plays first
    global current_player
    select_player = int(input('Choose who plays first.\n1 for Human and 2 for AI: '))

    # make sure correct selection is made
    while select_player not in range(1,3):
        select_player = int(input('Incorrect selection!\n Enter 1 for Human and 2 for AI: '))

    # set current player variable
    if select_player == 1:
        current_player[0] = 'Human'
    elif select_player == 2:
        current_player[0] = 'AI'

    # load game board
    load_board()


def load_board():
    os.system('clear')
    print('\n|' + board[0] + '|' + board[1] + '|' + board[2] + '|\n' +
          '|' + board[3] + '|' + board[4] + '|' + board[5] + '|\n' +
          '|' + board[6] + '|' + board[7] + '|' + board[8] + '|\n')

    play_game()


def change_player():
    global current_player

    if current_player[0] == 'AI':
        current_player[0] = 'Human'
    elif current_player[0] == 'Human':
        current_player[0] = 'AI'

    if current_player[1] == 'X':
        current_player[1] = 'O'
    elif current_player[1] == 'O':
        current_player[1] = 'X'


def	check_wins():
    # check if anyone has won
    global game_in_progress
    global won
    global winner
    global board
    global winning_blocks
    global draw

    # check rows
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 2 and 3'
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 2 and 3'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '4, 5 and 6'
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '4, 5 and 6'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '7, 8 and 9'
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '7, 8 and 9'
    # check columns
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 4 and 7'
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 4 and 7'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '2, 5 and 8'
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '2, 5 and 8'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '3, 6 and 9'
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '3, 6 and 9'
    # check diagnals
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 5 and 9'
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '1, 5 and 9'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '3, 5 and 7'
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        winner = current_player[0]
        game_in_progress = 0
        won = 1
        winning_blocks = '3, 5 and 7'
    elif board[0] != '-' and board[1] != '-' and board[2] != '-' and board[3] != '-' and board[4] != '-' and board[5] != '-' and board[6] != '-' and board[7] != '-' and board[8] != '-':
        draw = 1
        game_in_progress = 0
    else:
        game_in_progress = 1
        won = 0

def play_game():
    #start the game
    global game_in_progress
    global board
    global winner
    global won

    if game_in_progress == 0 and won == 0 and draw == 0:
        select_move = int(input(current_player[0] + ' plays first.\nSelect board position from 1 to 9: '))
    elif game_in_progress == 1 and won == 0 and draw == 0:
        select_move = int(input(current_player[0] + "'s turn.\nSelect board position from 1 to 9: "))
    elif game_in_progress == 0 and won == 1:
        print('GAME OVER! ' + winner + ' has won the game. The winning sections are\n' + winning_blocks)
        play_again()
    elif draw == 1:
        print('GAME OVER! It is a draw.')
        play_again()

    # make sure correct selection is made
    while select_move not in range(1,10):
        select_move = int(input('Incorrect selection!\nMake a selection between 1 and 9: '))
    while board[select_move - 1] != '-':
        select_move = int(input('You cannot play there, make another selection:  '))

    board[select_move - 1] = current_player[1]
    check_wins()
    change_player()
    load_board()

def play_again():
    global game_in_progress
    global won
    global winning_blocks
    global current_player
    global board

    play = int(input('Would you like to play again?\n1 for Yes and 2 for No: '))

    # make sure correct selection is made
    while play not in range(1,3):
        play = int(input('Incorrect selection!\n Enter 1 for Yes and 2 for No: '))

    if play == 1:
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        game_in_progress = 0
        won = 0
        current_player[0] = ''
        current_player[1] = 'X'
        winning_blocks = ''
        start_game()

    elif play == 2:
        print('\nGame ended. Thank you for playing.')
        quit()

# Begin the program
os.system('clear')
testlist = [1,2,3,5,3,1,2,1,6]
for position, item in enumerate(testlist):
    if item == 1:
        print(position)
start_game()