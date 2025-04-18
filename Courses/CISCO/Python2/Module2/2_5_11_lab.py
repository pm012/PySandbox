'''
Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.


'''
sudoky1 = ['295743861', #Yes
'431865927',
'876192543',
'387459216',
'612387495',
'549216738',
'763524189',
'928671354',
'154938672',]

sudoky2 = ['195743862', #No
'431865927',
'876192543',
'387459216',
'612387495',
'549216738',
'763524189',
'928671354',
'254938671',]


# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]    


def is_sudoky(board):
    # Check rows
    for row in board:
        if not checkset(row):
            return "No"

    # Check columns
    for col in range(9):
        column = ''.join(board[row][col] for row in range(9))
        if not checkset(column):
            return "No"

    # Check 3x3 sub-squares
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            square = ''
            for i in range(3):
                for j in range(3):
                    square += board[box_row + i][box_col + j]
            if not checkset(square):
                return "No"

    return "Yes"



if __name__ == "__main__":
    print(is_sudoky(sudoky1))
    print(is_sudoky(sudoky2))