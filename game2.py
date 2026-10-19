border = [
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7", 
          "8",
          "9",
         ]
# validate user input
players = {"x": "player 1",
           "o": "player 2"
           }
winning_combinations = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)
occupied = set()


def display_border():
    print()
    print(border[0], "|", border[1], "|", border[2])
    print("--+---+--")
    print(border[3], "|", border[4], "|", border[5])
    print("--+---+--")
    print(border[6], "|", border[7], "|", border[8])
    print()


def check_winner(symbol):
    print("checking_winner...")
    for combination in winning_combinations:
        if all(border[position] == symbol for position in combination):
            return True
    return False


def make_move(symbol):
    while True:
        choice = input(f"{players[symbol]} ({symbol}), choose a position (1-9): ")
        if not choice.isdigit():
            print("please enter a valid number.")
            continue
        position = int(choice) - 1
        if position < 0 or position > 8:
            print("please choose a position between 1 and 9.")
            continue
        if position in occupied:
            print("This position is already occupied.")
            continue
        border[position] = symbol
        occupied.add(position)
        break


#--- Main Game Loop (Must NOT be inside any function) ---
print("Welcome to Tic-Tac-Toe!")
current_player = "x"

while True:
    display_border()
    make_move(current_player)

    if check_winner(current_player):
        display_border()
        print(players[current_player], "Wins!")
        break

    if len(occupied) == 9:
        display_border()
        print("It's a draw!")
        break

    current_player = "o" if current_player == "x" else "x"

print("\nThanks for playing!")
