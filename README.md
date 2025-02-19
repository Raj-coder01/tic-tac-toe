# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. The game allows two players to take turns marking the spaces in a 3×3 grid with X and O, and it checks for winners or a draw after each move.

## How to Play

1. Clone the repository or download the script file.
2. Run the script using Python.
3. Follow the on-screen instructions to play the game.

## Functions

### `print_board(board)`
Prints the current state of the Tic-Tac-Toe board.

### `check_winner(board)`
Checks if there is a winner on the board. It returns the winning player's mark (X or O) if there is a winner, otherwise it returns `None`.

### `is_full(board)`
Checks if the board is full. It returns `True` if the board is full, otherwise it returns `False`.

### `tic_tac_toe()`
The main function to play the Tic-Tac-Toe game. It initializes the board, manages player turns, and checks for winners or a draw.
