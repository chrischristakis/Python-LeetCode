def valid_parentheses(s):
    stack = []

    for char in s:
        if char in '{([':
            stack.append(char)
            continue

        # If we're on a closing bracket, and the stack is empty, then invalid.
        if len(stack) == 0:
            return False

        popped = stack.pop()
        if (char == '}' and popped != '{') or \
                (char == ']' and popped != '[') or \
                (char == ')' and popped != '('):
            return False

    return len(stack) == 0


print(valid_parentheses('['))
print(valid_parentheses('[](){}'))
print(valid_parentheses('(]'))
print(valid_parentheses('[({[]})]'))
