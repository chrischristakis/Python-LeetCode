def makeGood(self, s):
    stack = []
    for c in s:
        stack.append(c)
        while len(stack) >= 2:
            top = stack.pop()
            if abs(ord(top) - ord(stack[-1])) == (ord('a') - ord('A')):
                stack.pop()
            else:
                stack.append(top)
                break

    return ''.join(stack)