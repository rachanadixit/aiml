# Tic-Tac-Toe game implementation

# Function to print the board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_winner(board, player):
    # All possible winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(space != " " for space in board)

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'.")
    print_board(board)

    while True:
        # Take input
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 9.")
            continue

        # Validate move
        if move < 0 or move > 8 or board[move] != " ":
            print("❌ Invalid move! Try again.")
            continue

        # Make move
        board[move] = current_player
        print_board(board)

        # Check for win
        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run the game
tic_tac_toe()
