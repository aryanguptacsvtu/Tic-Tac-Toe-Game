# Emojis for row headers
row_emojis = ["1️⃣ ", "2️⃣ ", "3️⃣ "]

def print_board(board):
    print("\n    1️⃣   2️⃣   3️⃣")  # Column headers
    print("    ------------")
    for i, row in enumerate(board):
        row_str = f"{row_emojis[i]} |"
        for value in row:
            row_str += f" {value} |"
        print(row_str)
        print("    ------------")


def get_move(turn, board):
    """
    Prompts the current player for a valid move.
    Checks for input correctness and whether the chosen cell is empty.
    """
    while True:
        try:
            print(f"\n👉 {turn}'s turn! Choose your move.")
            row = int(input("🔢 Enter row (1-3): "))
            col = int(input("🔢 Enter column (1-3): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        # Validating user input
        if row < 1 or row > 3:
            print("🚫 Invalid row. Please choose between 1 and 3.")
        elif col < 1 or col > 3:
            print("🚫 Invalid column. Please choose between 1 and 3.")
        elif board[row - 1][col - 1] != " ":
            print("🚫 Cell already taken. Try a different position.")
        else:
            break

    # Update board with the player's move
    board[row - 1][col - 1] = turn


def check_win(board, turn):
    """
    Checks all possible winning combinations for the current player.
    Returns True if there's a win; otherwise, False.
    """
    lines = [
        # Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        if all(board[row][col] == turn for row, col in line):
            return True
    return False


# Game initialization
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
turn = "X"          # Starting player
turn_number = 0     # Count of total turns played

print("🎉 Welcome to Tic-Tac-Toe! 🎉")
print_board(board)

# Main game loop
while turn_number < 9:
    get_move(turn, board)
    print_board(board)

    # Check if the current player has won
    if check_win(board, turn):
        print(f"\n🏆 Congratulations! Player {turn} wins! 🥳")
        break

    # Switch turn
    turn = "O" if turn == "X" else "X"
    turn_number += 1

# Check for draw
if turn_number == 9:
    print("\n🤝 It's a draw! Well played both players! ✌️")
