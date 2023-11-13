def daily_temperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i in range(0, len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res


print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
