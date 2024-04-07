def checkValidString(s):
    def recurse(i, curr='', count=0):
        if i == len(s):
            return count == 0

        if s[i] == '(':
            return recurse(i + 1, curr + '(', count + 1)
        elif s[i] == ')':
            if count < 0:
                return False
            return recurse(i + 1, curr + ')', count - 1)
        else:
            return recurse(i + 1, curr + '(', count + 1) or \
                   recurse(i + 1, curr + ')', count - 1) or \
                   recurse(i + 1, curr, count)

    return recurse(0)


def checkValidString(s):
    open = []
    stars = []
    for i, c in enumerate(s):
        if c == '(':
            open.append(i)
        elif c == ')':
            if open:
                open.pop()
            elif stars:
                stars.pop()
            else:
                return False
        else:
            stars.append(i)

    while open and stars:
        if open[-1] > stars[-1]:
            return False
        open.pop()
        stars.pop()

    return len(open) == 0
