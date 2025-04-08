# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

import random

def display_board(board):
    """Displays the Tic-Tac-Toe board in the required format."""
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def make_list_of_free_fields(board):
    """Returns a list of free fields (row, col) on the board."""
    return [(r, c) for r in range(3) for c in range(3) if isinstance(board[r][c], int)]

def enter_move(board):
    """Gets the user's move and updates the board."""
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid input. Choose a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if not isinstance(board[row][col], int):
                print("This space is already taken. Try again.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def draw_move(board):
    """Handles the computer's move, placing 'X' randomly on a free field."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def check_victory(board, sign):
    """Checks if a player has won the game."""
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def tic_tac_toe():
    """Runs the Tic-Tac-Toe game loop."""
    board = [[(3 * r + c + 1) for c in range(3)] for r in range(3)]
    board[1][1] = 'X'  # Computer starts in the center
    
    while True:
        display_board(board)
        if check_victory(board, 'X'):
            print("Computer wins!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        
        enter_move(board)
        display_board(board)
        if check_victory(board, 'O'):
            print("You win!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        
        draw_move(board)

tic_tac_toe()
