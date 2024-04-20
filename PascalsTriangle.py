def generate(numRows):
    dp = [[1]]

    # start from second row
    for row in range(1, numRows):
        res = [1] * (row + 1)
        for i in range(1, row):
            res[i] = dp[-1][i - 1] + dp[-1][i]
        dp.append(res)
    return dp


print(generate(5))
