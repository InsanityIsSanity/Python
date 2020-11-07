import random

welcome_text = "Welcome to the Hangman game, your random word has been selected by the AI:"
word_list = ["water fountain", "artificial intelligence", "computer hardware", "flat earth"]
word = ''
word_len = 0
revealed_word = []
hidden_word = []
lives = 0


def create_word():
    global revealed_word, hidden_word, word, word_len, revealed_word, hidden_word, lives

    lives = 0
    revealed_word = []
    hidden_word = []

    word = word_list[random.randint(0, len(word_list) - 1)]
    word_len = len(word)

    for letter in word:
        hidden_word.append(letter)

    for letter in word:
        if letter != " ":
            revealed_word.append("-")
        else:
            revealed_word.append(letter)
    check_input()


def lose_game():
    print("You have run out of guesses. Game Over")
    exit()


def check_turn():
    global lives

    check_win()

    if lives < 6:
        print(f"{6 - lives} lives left")
    elif lives == 6:
        print("Last turn!")
    else:
        lose_game()


def update_revealed_word(x):
    global revealed_word

    for index, letter in enumerate(word):
        if x == letter:
            revealed_word[index] = letter


def play(letter):
    global lives
    count = 0

    if letter in revealed_word:
        print("You have already revealed that letter. Try again!")
        check_input()
    else:
        if letter in word:
            for l in word:
                if l == letter:
                    count += 1
            print(f"Well done, '{letter}' was found {count} times.")
            update_revealed_word(letter)
            check_input()
        else:
            print(f"Sorry, '{letter}' was not found.")
            lives += 1
            check_input()


def check_win():
    if hidden_word == revealed_word:
        print("Congratulations, you win.")
        choice = input("Would you like to play again?")
        if choice == "yes":
            create_word()
        elif choice == "no":
            exit()
        else:
            check_win()


def check_input():
    print()
    print(*revealed_word)
    print()
    check_turn()
    while True:
        guess = input("Enter a letter: ")
        if len(guess) > 1:
            print("Only 1 letter at a time cowboy!")
            continue
        else:
            break
    play(guess)


print(welcome_text)
print("*" * len(welcome_text), "\n")
create_word()



