from random import randint

# display game rules
print("welcome to Rock - Paper - Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # validate user input
    try:
        choice = int(input("Enter your choice (1/2/3):"))
        if choice not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # User choice
    player = choices[choice - 1]
    print("\nUser choice is:", player)
    print("Now it's Computer's Turn...")

    # Computer choice
    comp_choice = randint(1, 3)
    computer = choices[comp_choice - 1]
    print("Computer choice is:", computer)
    print(player, "vs", computer)

    # Determine the winner
    if choice == comp_choice:
        print("<== It's a Tie! ==>")
    elif (
        (choice == 1 and comp_choice == 3)
        or (choice == 2 and comp_choice == 1)
        or (choice == 3 and comp_choice == 2)
    ):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # play again?
    answer = input("\nDo you want to play again? (y/n):").lower()
    while answer not in ["y", "n"]:
        print("please enter y or n.")
        answer = input("\nDo you want to play again? (y/n):").lower()

    if answer == "n":
        print("\nThanks for playing!")
        break


