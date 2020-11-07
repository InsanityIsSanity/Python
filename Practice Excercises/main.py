import time

print('Welcome to the Whole Foods Market Bastard Program.')
# input('Press RETURN when youre ready to begin.')
print('Loading employee file...\n')
# time.sleep(1)

file = open('text.txt', 'r')
tm_list = []
tm_fields = []
tm_found = 0
name = ''


for tm in file:
    split_list = tm.split()
    tm_list.append(split_list)


def start():
    global name, tm_found
    while True:
        try:
            name = input('Please enter your name: ')
        except ValueError:
            continue
        else:
            loaded_tm = []
            for i, elem in enumerate(tm_list):
                for field in elem:
                    if name.lower() in str(elem).lower():
                        tm_found = 1
                        loaded_tm.append(field)
                    else:
                        break
            break

    if tm_found == 1:
        print(f'I found your profile {name}, welcome to your online work portal.')
        tm_dashboard(loaded_tm, 8)
    elif tm_found == 0:
        print(f'Sorry {name}, I couldnt find you on our employee list, are you sure you work here? Please '
            f'either try again or type EXIT to quit. ')
        start()


def main_menu(loaded_tm):
    field_name = ''
    print()
    print('*' * 25)
    for index, field in enumerate(loaded_tm):
        if index == 0:
            field_name = 'First Name:'
        elif index == 1:
            field_name = 'Surname:'
        elif index == 2:
            field_name = 'Team Member ID:'
        print(index + 1, field_name, field)
    print('\n9 Edit Details')
    print('0 Exit')
    print('*' * 50)
    print()
    while True:
        try:
            load = int(input('What would you like to do: '))
        except ValueError:
            print('Numbers only please, try again.')
            continue
        else:
            if load in range(1, 10):
                if load == 9:
                    tm_dashboard(loaded_tm, 9)
                else:
                    print('Wrong choice.')
                    pass
            else:
                end()


def edit_menu(loaded_tm):
    field_name = ''
    print()
    print('*' * 25)
    for index, field in enumerate(loaded_tm):
        if index == 0:
            field_name = 'Edit First Name:'
        elif index == 1:
            field_name = 'Edit Surname:'
        elif index == 2:
            field_name = 'Edit Team Member ID:'
        print(index + 1, field_name, field)
    print('\n9 View Details')
    print('0 Exit')
    print('*' * 50)
    print()
    while True:
        try:
            load = int(input('What would you like to do: '))
        except ValueError:
            print('Numbers only please, try again.')
            continue
        else:
            if load in range(1, 10):
                if load == 1:
                    tm_dashboard(loaded_tm, 1)
                elif load == 2:
                    tm_dashboard(loaded_tm, 2)
                elif load == 3:
                    tm_dashboard(loaded_tm, 3)
                elif load == 9:
                    tm_dashboard(loaded_tm, 8)
                else:
                    print('Wrong choice.')
                    pass
            else:
                end()


def tm_dashboard(loaded_tm, load):
    if load == 8:
        main_menu(loaded_tm)
    elif load == 9:
        edit_menu(loaded_tm)
    elif load == 1:
        edit_tm(loaded_tm, 'name')
    elif load == 2:
        edit_tm(loaded_tm, 'surname')
    elif load == 3:
        edit_tm(loaded_tm, 'tmid')
    elif load == 0:
        pass


def edit_tm(loaded_tm, field):
    global name

    if field == 'name':
        print(f'Current Name: {loaded_tm[0]}')
        new_name = input('Enter your new Name: ')
        loaded_tm[0] = new_name
        name = new_name
        print('Your Name has been updated.')
        edit_menu(loaded_tm)
    elif field == 'surname':
        print(f'Current Surname: {loaded_tm[1]}')
        new_surname = input('Enter your new Surname: ')
        loaded_tm[1] = new_surname
        print('Your Surname has been updated.')
        edit_menu(loaded_tm)
    elif field == 'tmid':
        print(f'Current TM ID: {loaded_tm[2]}')
        while True:
            try:
                new_tmid = int(input('Enter your new TM ID: '))
            except ValueError:
                print('Your TM ID can only contain numbers.')
                continue
            else:
                code = 5533
                while True:
                    try:
                        code_pass = int(input('Please enter PRS passcode to authorize this change or type 0 to go back: '))
                    except ValueError:
                        print('The passcode is numerical.')
                        continue
                    else:
                        if code_pass != code:
                            if code_pass == 0:
                                main_menu(loaded_tm)
                            else:
                                print('INCORRECT PASSCODE')
                                continue
                        else:
                            print('Your TM ID has been updated.')
                            loaded_tm[2] = new_tmid
                            # save = open('text.txt', 'w')
                            break
                print(tm_list)
                main_menu(loaded_tm)


def end():
    print(f'Goodbye {name}.')
    exit()


start()