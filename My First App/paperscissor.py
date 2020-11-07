import time
import random

end_game_choices = ['Play again', 'Exit to the Main Menu']
choices = ['Rock', 'Paper', 'Scissor', 'r', 'p', 's']
high_low_choices = ['high', 'h', 'low', 'l']
current_player = ''
game_count = 0
ai_wins = 0
player_wins = 0
min_num = 1
max_num = 10
random_num = random.randint(1, 10)
turn = 2
ai_move = 0
player_move = 0
hand_count = 0
player_name = ''
total_turns = 5


def app1_rock_paper(user_name):
    global turn, player_name, total_turns
    player_name = user_name

    print(f'Welcome to the Rock, Paper & Scissor game {user_name}. You will be playing against the AI.')
    while True:
        try:
            total_turns = int(input('How many hands would you like to play? '))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        else:
            break
    print(f'The game will last {total_turns} rounds.\n')
    print(f'We will roll a number between {min_num} and {max_num}, who ever guesses correctly will play first.')
    high_low_choice = input('Will you guess High or Low:').casefold()

    while high_low_choice not in high_low_choices:
        high_low_choice = input('Incorrect choice, try again. Will you guess High or Low:').casefold()

    if high_low_choice == 'l'.casefold() or high_low_choice == 'low'.casefold():
        high_low_choice = 'low'
    else:
        high_low_choice = 'high'

    print(f'\nYou have chosen to go {high_low_choice}...')
    print('Rolling in 3')
    time.sleep(1)
    print('Rolling in 2')
    time.sleep(1)
    print('Rolling in 1')
    time.sleep(1)
    print(f'Random number: {random_num}\n')
    if high_low_choice == 'low' and random_num in range(min_num, (max_num // 2) + 1):
        print('You guessed correct, you play first.\n')
        turn = 1
        time.sleep(1)
        start_game()
    elif high_low_choice == 'high' and random_num in range((max_num // 2) + 1, max_num):
        print('You guessed correct, you play first.\n')
        turn = 1
        time.sleep(1)
        start_game()
    else:
        print('You guessed incorrectly, AI plays first.\n')
        turn = 0
        time.sleep(1)
        start_game()


def start_game():
    global ai_move, player_move, turn, game_count, hand_count, ai_wins, player_wins

    while game_count < total_turns:
        while hand_count < 2:
            if turn == 0:
                ai_move = random.randint(0, 2)
                print(f'AI has played its turn. ')
                turn = 1
                hand_count += 1
            elif turn == 1:
                player_turn_str = input('Rock, Paper or Scissors?')

                while player_turn_str not in choices:
                    player_turn_str = input('Incorrect choice, try again. Rock, Paper or Scissors?')

                if player_turn_str == 'Rock'.casefold() or player_turn_str == 'R'.casefold():
                    player_move = 0
                elif player_turn_str == 'Paper'.casefold() or player_turn_str == 'P'.casefold():
                    player_move = 1
                elif player_turn_str == 'Scissors'.casefold() or player_turn_str == 'S'.casefold():
                    player_move = 2

                turn = 0
                hand_count += 1
        game_count += 1
        hand_count = 0
        # Check who won the hand
        if ai_move == 0 and player_move == 0:
            winner = 'Draw'
        elif ai_move == 0 and player_move == 1:
            player_wins += 1
            winner = 'Player'
        elif ai_move == 0 and player_move == 2:
            ai_wins += 1
            winner = 'AI'
        elif ai_move == 1 and player_move == 0:
            ai_wins += 1
            winner = 'AI'
        elif ai_move == 1 and player_move == 1:
            winner = 'Draw'
        elif ai_move == 1 and player_move == 2:
            player_wins += 1
            winner = 'Player'
        elif ai_move == 2 and player_move == 0:
            player_wins += 1
            winner = 'Player'
        elif ai_move == 2 and player_move == 1:
            ai_wins += 1
            winner = 'AI'
        elif ai_move == 2 and player_move == 2:
            winner = 'Draw'
        print(f'You played {choices[player_move]} and AI played {choices[ai_move]}.\n')
        print('*' * 50)
        print(f'End of hand {game_count}/{total_turns} - The winner is {winner}')
        print('*' * 50)
        print()
    print(f'End of game.')
    print(f'Total wins for Player: {player_wins}')
    print(f'Total wins for AI: {ai_wins}')
    print(f'Total Draws: {total_turns - (player_wins + ai_wins)}\n')
    end_game()


def end_game():
    global turn, ai_move, ai_wins, player_move, hand_count, game_count, player_wins, current_player
    print('*' * 50)
    for index, option in enumerate(end_game_choices):
        print(f'{index + 1} {option}')
    print('*' * 50)
    print()
    while True:
        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        else:
            break
    if choice in range(1, 3):
        if choice == 1:
            turn = 2
            ai_move = 0
            player_move = 0
            hand_count = 0
            current_player = ''
            game_count = 0
            ai_wins = 0
            player_wins = 0
            app1_rock_paper(player_name)
        else:
            from start import menu
            menu()
    else:
        end_game()





