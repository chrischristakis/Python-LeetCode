def removeDigit(number, digit):
    max_num = 0
    for i in range(len(number)):
        if number[i] == digit:
            removed = int(number[:i] + number[i + 1:])
            max_num = max(max_num, removed)
    return str(max_num)

