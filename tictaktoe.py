import random

# Initialize the board
board = [" " for _ in range(9)]

# Display the board
def display_board():
    print("\n")
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print("|".join(row))
        print("-" * 5)
    print("\n")

# Check for a win
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

# Check if the board is full
def is_full():
    return " " not in board

# AI move (medium difficulty)
def ai_move():
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "
    # Try to block
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "
    # Random move
    move = random.choice([i for i in range(9) if board[i] == " "])
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, computer is O.")
    display_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("That spot is already taken.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Choose between 1 and 9.")
            continue
        board[move] = "X"

        display_board()
        if check_winner("X"):
            print("You win! 🎉")
            break
        if is_full():
            print("It's a tie!")
            break

        # AI move
        ai_move()
        display_board()
        if check_winner("O"):
            print("Computer wins! 🤖")
            break
        if is_full():
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()