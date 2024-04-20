def findFarmland(self, land):
    res = []
    m = len(land)  # rows
    n = len(land[0])  # cols

    for row in range(0, m):
        for col in range(0, n):
            if land[row][col] == 0:
                continue

            # find the right most farm cell
            col2 = col
            while col2 < n and land[row][col2] != 0:
                col2 += 1
            col2 -= 1  # we overshoot in both cases, so remove 1 index.

            # find bottom most farm cell
            row2 = row
            while row2 < m and land[row2][col2] != 0:
                row2 += 1
            row2 -= 1

            res.append([row, col, row2, col2])

            # replace land we visited with zeroes so we dont visit again.
            for r in range(row, row2 + 1):
                for c in range(col, col2 + 1):
                    land[r][c] = 0

    return res
