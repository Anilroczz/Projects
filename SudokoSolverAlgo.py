# display() method is used to display the grid. It takes grid as an input and displays it to the screen.
def display(board):
    for i in range(0,9):
        for j in range(0,9):
            print(board[i][j], end=" ")
        print()

# solve() method is used to check whether a number is valid in the respective position.
def solve(board, row, col, num):

    # loops through elements in a particular row to find a match. if match occurs , returns false.
    for i in range(0, 9):
        if board[row][i] == num:
            return False

    # loops through elements in a particular column to find a match. if match occurs , returns false.
    for i in range(0, 9):
        if board[i][col] == num:
            return False

    startRow = row - row % 3       # startRow is used to get relative position of the the element in the rows of grid.
    startCol = col - col % 3       # startCol is used to get relative position of the the element in the columns of grid.

    # loops through the sub-grid of size 3*3 to find a match. if match occurs , returns false.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[startRow+i][startCol+j] == num:
                return False

    # if all checks above satisfies , it returns true.
    return True

def sudokoSolver(board,row,col) :
    #  The below case returns true , if all the rows and columns of the grid are validated.
    if row == 8 and col == 9:
        return True

    # The below case is referred when all the elements in a row are validated.
    # row count is incremented by 1 and column count is set back to 0.
    if col == 9:
        row += 1
        col = 0

    # The below refers when the element is given in the position.
    # In this case, the column count s incremented by 1.
    if board[row][col] > 0:
        return sudokoSolver(board, row, col+1)

    # The loop checks the values in range 1-9 to insert into grid.
    # If number validates, It inserts the number.
    for num in range(1, 10, 1):
        if solve(board, row, col, num) :
            board[row][col] = num
            if sudokoSolver(board, row, col+1):
                return True
        board[row][col] = 0

    # if a grid doesn't satisfy any of the above conditions , it implies that the grid is non-solvable.
    return False


# example sudoku problems.
board1 = [[0, 7, 2, 0, 0, 4, 0, 5, 3],
          [0, 4, 9, 0, 1, 0, 0, 8, 2],
          [8, 0, 0, 2, 5, 7, 9, 6, 0],
          [0, 0, 0, 7, 4, 0, 0, 0, 0],
          [0, 0, 7, 8, 0, 0, 6, 4, 9],
          [0, 8, 4, 0, 9, 0, 3, 0, 5],
          [9, 2, 0, 0, 6, 1, 0, 3, 0],
          [0, 0, 0, 4, 0, 0, 0, 1, 0],
          [0, 0, 0, 3, 7, 8, 0, 9, 0]]

board2 =  [[2, 5, 0, 0, 3, 0, 9, 0, 1],
          [0, 1, 0, 0, 0, 4, 0, 0, 0],
          [4, 0, 7, 0, 0, 0, 2, 0, 8],
          [0, 0, 5, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 9, 8, 1, 0, 0],
          [0, 4, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 3, 6, 0, 0, 7, 2],
          [0, 7, 0, 0, 0, 0, 0, 0, 3],
          [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if sudokoSolver(board1, 0, 0):
    display(board1)
else:
    print("Grid is non-solvable")

print()

if sudokoSolver(board2, 0, 0):
    display(board2)
else:
    print("Grid is non-solvable")
