def app4_file_mod(user_name):
    file_handle()


def file_handle(name, mode):
    file_name = name 
    file_mode = mode
    file = open(f'{file_name}.txt', f'{file_mode}')

    if file_mode == 'r':
        file_content = file.read()
        print(file_content)

    elif file_mode == 'w+':
        while True:
            try:
                scissor_game_wins = int(input('How many Scissor Game Wins to add: '))
            except ValueError:
                print('Sorry, incorrect choice, numbers only please!')
                continue
            else:
                file.write(f'Scissor Game Wins: {scissor_game_wins}\n')
                break

        while True:
            try:
                scissor_game_losses = int(input('How many Scissor Game Losses to add: '))
            except ValueError:
                print('Sorry, incorrect choice, numbers only please!')
                continue
            else:
                file.write(f'Scissor Game Losses: {scissor_game_losses}\n')
                break

        while True:
            try:
                guess_game_wins = int(input('How many Guess Game Wins to add: '))
            except ValueError:
                print('Sorry, incorrect choice, numbers only please!')
                continue
            else:
                file.write(f'Guess Game Wins: {guess_game_wins}\n')
                break

        while True:
            try:
                guess_game_losses = int(input('How many Guess Game Losses to add: '))
            except ValueError:
                print('Sorry, incorrect choice, numbers only please!')
                continue
            else:
                file.write(f'Guess Game Losses: {guess_game_losses}\n')
                break

        while True:
            try:
                total_app_load = int(input('How many Total Loads (app) to add: '))
            except ValueError:
                print('Sorry, incorrect choice, numbers only please!')
                continue
            else:
                file.write(f'Total App Loads: {total_app_load}\n')
                break

    elif file_mode == 'a+':
        pass

    file.close()
    print('\nFile Closed. Returning to Main Menu.')

def start():
    print('*' * 30)
    print('\t\t\t\t\t\t\t\t')
    print('1 Update File Information')
    print('2 Overwrite File Information')
    print('3 Read File Content\n')
    print('0 Exit Application')
    print('\t\t\t\t\t\t\t\t')
    print('*' * 30, '\n')

    while True:
        try:
            choice = int(input('Please select an option from the menu above: '))
        except ValueError:
            print('Sorry I didnt understand that! Try again.\n')
            continue
        else:
            if choice in range(0, 4):
                if choice == 0:
                    print('You have chosen to exit, goodbye!')
                    break
                elif choice == 1:
                    print('UPDATE MODE ACTIVE\n')
                    name = str(input('Please enter your file name: '))
                    file_handle(name, 'a+')
                elif choice == 2:
                    print('OVERWRITE MODE ACTIVE\n')
                    name = str(input('Please enter your file name: '))
                    file_handle(name, 'w+')
                elif choice == 3:
                    print('READ MODE ACTIVE\n')
                    name = str(input('Please enter your file name: '))
                    file_handle(name, 'r')
            else:
                print('Sorry, that choice is not valid.')
                continue

app4_file_mod('user_name')