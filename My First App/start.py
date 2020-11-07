from os import system, name
from time import sleep
from paperscissor import app1_rock_paper
from numguess import app2_num_guess
from shoplist import app3_shop_list
from filemod import app4_file_mod

available_apps = ['Rock Paper Scissor Game',
                  'Number Guessing Game',
                  'Shopping List Generator',
                  'File Modifier']
available_apps_index = []
global app_index_plus, user_name

for index, value in enumerate(available_apps):
    available_apps_index.append(index + 1)


def start():
    global user_name

    user_name = input('Please enter your name: ')
    print(f'Welcome to my first Python program {user_name}.\n')
    menu()


def menu():
    global app_index_plus
    for app_index, app in enumerate(available_apps):
        app_index_plus = app_index + 1
        available_apps_index.append(app_index_plus)
        print(app_index_plus, app)
    print('*' * 50)
    print('0 Exit')
    print('*' * 50, '\n')

    while True:
        try:
            choice = int(input("Please select the application you would like to load from the list above: "))
        except ValueError:
            print("Sorry, I didn't understand that!")
            continue
        else:
            break

    if choice in range(0, app_index_plus + 1):
        if choice == 1:
            app1_rock_paper(user_name)
            print('\n' * 9)
        elif choice == 2:
            app2_num_guess(user_name)
            print('\n' * 9)
        elif choice == 3:
            app3_shop_list(user_name)
            print('\n' * 9)
        elif choice == 4:
            app4_file_mod(user_name)
            print('\n' * 9)
        elif choice == 0:
            print(f'You have chosen to exit the game. Goodbye {user_name}.')
    else:
        menu()


menu()