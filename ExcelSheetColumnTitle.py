def convertToTitle(columnNumber):
    def char_from_num(x):
        return chr(ord('A') + x)

    title = ""
    while columnNumber > 0:
        columnNumber -= 1  # Since A -> 1, we want A -> 0
        curr = columnNumber % 26  # Least sig figure
        title += char_from_num(curr)
        columnNumber /= 26  # Shift to next sig figure
    return title[::-1]
