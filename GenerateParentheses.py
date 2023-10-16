def generate_parentheses(n):
    res = []

    def recursive(open, closed, str):
        if open < n:
            recursive(open + 1, closed, str + '(')
        if closed < open:
            recursive(open, closed + 1, str + ')')
        if open == closed == n:
            res.append(str)

    recursive(0, 0, '')
    return res


print(generate_parentheses(5))
