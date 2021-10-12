def checker(box) :
    is_valid = False
    for arr in box :
        if sum(arr) == 45 and len(set(arr)) == 9 :
            for ele in arr :
                if ele >= 1 and ele <= 9 :
                    is_valid = True
                else :
                    return False
        else :
            is_valid = False
            break
    return is_valid

def row_checker(board) :
    box = board[:]
    return checker(box)

def column_checker(board) :
    box = []
    for i in range(len(board)) :
        col = []
        for j in range(len(board)) :
            col.append(board[j][i])
        box.append(col)
    return checker(box)

def subgrid_checker(board) :
    box = []
    shift = 3
    for i in range(0,len(board),shift) :
        for j in range(0,len(board),shift) :
            lst = []
            for k in range(i,i+shift) :
                lst = lst + board[k][j:j+shift]
            box.append(lst)
    return checker(box)






def sudoko_checker(board) :
    is_row = row_checker(board)             # checks for row validation
    is_column = column_checker(board)       # checks for column validation
    is_grid = subgrid_checker(board)        # checks for sub-grid validation

    if is_row and is_column and is_grid :
        return True
    else :
        return False

board1 =  [[5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
board2 = [[1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9],
          [1,2,3,4,5,6,7,8,9]]

print(subgrid_checker(board1))
print(sudoko_checker(board2))