def game(board):
    """
    use 2 bits per cell instead of one, left is future, right is current.
    00 < was dead, is dead
    01 < was alive, is dead
    10 < was dead is alive
    11 < was alive is alive
    """

    m = len(board)  # rows
    n = len(board[0])  # cols

    for row in range(m):
        for col in range(n):
            alive = board[row][col]

            # get neighbours state bounded by border
            left_bound = max(0, col-1)
            right_bound = min(n, col+2)
            top_bound = max(0, row-1)
            bot_bound = min(m, row+2)
            living_neighbors = 0
            for nrow in range(top_bound, bot_bound):
                for ncol in range(left_bound, right_bound):
                    if nrow == row and ncol == col:
                        continue

                    # select right bit (current state) and add to our counter if its alive.
                    living_neighbors += board[nrow][ncol] & 0b1

            # handle cases where cell becomes or stays living
            if not alive and living_neighbors == 3:
                board[row][col] |= 0b10
            if alive and 2 <= living_neighbors <= 3:
                board[row][col] |= 0b10

    for row in range(m):
        for col in range(n):
            board[row][col] >>= 1


boardd = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game(boardd)
print(boardd)
