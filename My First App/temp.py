import time
random_num = 5
min_num = 1
max_num = 10

high_low_choice = input('Will you guess High or Low:').casefold()

if high_low_choice == 'l'.casefold() or high_low_choice == 'low'.casefold():
    high_low_choice = 'low'
else:
    high_low_choice = 'high'

print(f'\nYou have chosen to go {high_low_choice}...')

print(f'Random number: {random_num}\n')
if high_low_choice == 'low' and random_num in range(min_num, (max_num // 2) + 1):
    print('You guessed correct, you play first.\n')
elif high_low_choice == 'high' and random_num in range((max_num // 2) + 1, max_num):
    print('You guessed correct, you play first.\n')
else:
    print('You guessed incorrectly, AI plays first.\n')

# this is added to test github sync settings
