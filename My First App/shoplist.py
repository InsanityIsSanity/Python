global user_item_list, item_list, total

item_list = {'Eggs': 2.50, 'Bread': 1.50, 'Milk': 1.00, 'Candy': 3.00}
user_item_list = {}
total = 0.00


def app3_shop_list(user_name):
    player_name = user_name
    print(f'Welcome to the Shopping List application {user_name}, where you can add items to your shopping list.\n')
    available_items()
    print()
    print()
    user_list_print()


def available_items():
    print('*' * 27)
    print('**\t ', 'AVAILABLE ITEMS', '\t **')
    print('*' * 27)
    for key in sorted(item_list):
        print('**\t', key, '\t\t', item_list[key], '\t **')
    print('**', ('\t' * 6), '**')
    print('*' * 27)


def user_list():
    global total
    user_add = input('\nWhich item would you like to add to your list? ')
    while user_add not in item_list:
        user_add = input('Incorrect choice, please choose from the available items in the list above.')
        continue

    while True:
        try:
            count = int(input(f'How many {user_add} would you like to add to your list? '))
        except ValueError:
            print('Sorry I only understand numbers! ')
            continue
        else:
            break
    price = item_list.get(f'{user_add}')
    user_item_list[f'{user_add}'] = count
    total = total + (count * price)

    print(f'\n{count} {user_add} added to your shopping list.\n')
    available_items()
    print()
    print()
    user_list_print()


def user_list_print():
    print('*' * 27)
    print('**\t\t', 'YOUR ITEMS', '\t **')
    print('*' * 27)
    for key in sorted(user_item_list):
        print('**\t', key, '\t\t', user_item_list[key], '\t\t **')
    print('*' * 27)
    print('**\t', 'Total', '\t\t', total, '\t **')
    print('*' * 27)
    user_list()



