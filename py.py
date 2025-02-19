def print_board(board):
    """Function to print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Function to check if there is a winner."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]  # Column win

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # Diagonal win

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # Diagonal win

    return None


def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn % 2]}'s turn")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        board[row][col] = players[turn % 2]
        winner = check_winner(board)

        if winner
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1


if _name_ == "_main_":
    tic_tac_toe()
