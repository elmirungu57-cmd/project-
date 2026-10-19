from random import randint

attempts = 7


def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print("you have 7 attempts to guess it.\n")


def play_game(number, attempt=1):
    if attempt > attempts:
        print("\nGame Over!")
        print("The correct number was:", number)
        return

    guess = input(f"Attempt {attempt}/{attempts} - Enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("please enter a number between 1 and 100,\n")
        return play_game(number, attempt)

    if guess == number:
        print("\ncongratulations! you guessed the correct number!")
        print("you guessed it in", attempt, "attempt(s).")
        return
    elif guess < number:
        print("Too low! Try a higher number.\n")
    else:
        print("Too High! Try a lower number.\n")

    return play_game(number, attempt + 1)


# start the game
display_rules()
random_number = randint(1, 100)
play_game(random_number)
