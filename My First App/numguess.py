import random
import time
player_name = ''


def app2_num_guess(user_name):
    global player_name
    player_name = user_name
    print(f'Welcome to the Number Guessing game {user_name}. You will be playing against the AI.')
    print('*' * 50)
    print('1 AI should guess')
    print('2 Player will guess')
    print('*' * 50)
    while True:
        try:
            choice = int(input('Who should try to guess first?'))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        else:
            if choice == 1 or choice == 2:
                break
            continue
    if choice == 1:
        print('AI will try to guess a number the player is thinking of.')
        start_game(1)
    elif choice == 2:
        print('Player will try to guess a number the AI is thinking of.')
        start_game(2)


def start_game(guesser):
    if guesser == 1:
        ai_turns = 0
        while True:
            try:
                min_num = int(input('Please define the lowest number: '))
            except ValueError:
                print('Sorry, please enter a valid number.')
                continue
            else:
                break
        while True:
            try:
                max_num = int(input('Please define the highest number: '))
            except ValueError:
                print('Sorry, please enter a valid number.')
                continue
            else:
                break
        input('\nPress any key when you are ready to begin.')
        ai_guess = random.randint(min_num, max_num)
        while True:
            try:
                print(f'The AI guesses your number to be {ai_guess}.')
                choice = str(input('Is this [C]Correct, should I guess [H]igher or [L]ower? ').casefold())
            except ValueError:
                print('Incorrect selection.')
                continue
            else:
                if choice in 'chl':
                    if choice == 'c':
                        ai_turns += 1
                        print(f'The AI has guessed correctly and wins using {ai_turns} guesses.')
                        break
                    elif choice == 'h':
                        if min_num == max_num or min_num > max_num:
                            print('Youre cheating now. The AI has left the game!')
                            break
                        min_num = ai_guess
                        ai_guess = (min_num + max_num) // 2
                        continue
                    elif choice == 'l':
                        if min_num == max_num or min_num > max_num:
                            print('\nYoure cheating now. The AI has left the game!')
                            break
                        max_num = ai_guess
                        ai_guess = (min_num + max_num) // 2
                        continue
                else:
                    print('Incorrect selection.')
                    continue
        end_game()

    elif guesser == 2:
        player_turns = 0
        while True:
            try:
                min_num = int(input('Please define the lowest number: '))
            except ValueError:
                print('Sorry, please enter a valid number.')
                continue
            else:
                break
        while True:
            try:
                max_num = int(input('Please define the highest number: '))
            except ValueError:
                print('Sorry, please enter a valid number.')
                continue
            else:
                break
        print('\nThe AI is thinking of a number')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        ai_number = random.randint(min_num, max_num)
        print('The AI is ready.')
        while True:
            try:
                player_guess = int(input(f'Please guess a number between {min_num} and {max_num}: '))
            except ValueError:
                print('Sorry, please enter a valid number.')
                continue
            else:
                if player_guess < min_num or player_guess > max_num:
                    print(f'Your guess is out of range.')
                    continue
                else:
                    player_turns += 1
                    if player_guess == ai_number:
                        print(f'Congratulations, you won using {player_turns} guesses.')
                        break
                    else:
                        if player_guess > ai_number:
                            print('Wrong! You need to guess Lower.')
                            continue
                        elif player_guess < ai_number:
                            print('Wrong! You need to guess Higher.')
                            continue
        end_game()


def end_game():
    print('*' * 50)
    print('1 Play again')
    print('2 Exit to main menu')
    print('*' * 50)
    print()
    while True:
        try:
            choice = int(input('What would you like to do? '))
        except ValueError:
            print('Sorry, please enter a valid number.')
            continue
        else:
            if choice not in range(1, 3):
                print('Sorry, please enter a valid number.')
                continue
            elif choice == 1:
                app2_num_guess(player_name)
            elif choice == 2:
                from start import start
                start()
