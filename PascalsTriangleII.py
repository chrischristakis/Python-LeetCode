# O(n) space, can modify in place due to onyl caring about current and previous element to alter current one
def getRowBetter(rowIndex):
    row = [1] * (rowIndex + 1)  # initialize all 1's

    for i in range(0, rowIndex + 1):
        for j in range(i - 1, 0, -1):  # iterate backwards between last and first element of row
            row[j] = row[j] + row[j - 1]
    return row


# O(n!) space
def getRow(rowIndex):
    row = []

    for i in range(0, rowIndex + 1):
        temp = row[:]
        temp.append(1)

        for j in range(1, i):
            temp[j] = row[j] + row[j - 1]
        row = temp

    return row
