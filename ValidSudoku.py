def valid_sudoku(board):
    # process rows
    for row in range(9):
        unique = set()
        for col in range(9):
            if board[row][col] in unique:
                return False
            if board[row][col] != '.':
                unique.add(board[row][col])

    # process cols
    for col in range(9):
        unique = set()
        for row in range(9):
            if board[row][col] in unique:
                return False
            if board[row][col] != '.':
                unique.add(board[row][col])

    # process chunks
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            unique = set()
            for chunk_row in range(row, row + 3):
                for chunk_col in range(col, col + 3):
                    if board[chunk_row][chunk_col] in unique:
                        return False
                    if board[chunk_row][chunk_col] != '.':
                        unique.add(board[chunk_row][chunk_col])

    return True


def valid_sudoku2(board):
    row_list = {}
    col_list = {}
    chunk_list = {}
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == '.':
                continue

            val = int(board[row][col]) - 1  # subtract 1 since numbers are 1-9, we want 0-8 for indexing

            # We have 9 chunks indexed [0,8], this formula calculates which chunk index (row,col) is in
            chunk_index = (3 * (row // 3)) + (col // 3)

            if (row,val) in row_list or (col, val) in col_list or (chunk_index, val) in chunk_list:
                return False

            row_list[(row,val)] = col_list[(col,val)] = chunk_list[(chunk_index,val)] = 1

    return True


print(valid_sudoku2(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
))
print(valid_sudoku2(
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
))

