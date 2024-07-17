def titleToNumber(columnTitle):
    num = 0
    for i in range(0, len(columnTitle)):
        digit = ord(columnTitle[i]) - ord('A')
        num = num * 26 + (digit + 1)  # Shift by tens place, add ditig + 1 since A->1, not A->0
    return num