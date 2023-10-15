def eval_rpn(tokens):
    stack = []

    for op in tokens:
        if op not in '+/*-':
            stack.append(int(op))
            continue

        right_op = stack.pop()
        left_op = stack.pop()
        if op == '+':
            stack.append(left_op + right_op)
        elif op == '-':
            stack.append(left_op - right_op)
        elif op == '*':
            stack.append(left_op * right_op)
        else:
            stack.append(int(float(left_op) / right_op))

    # Last element will be the result of RPN (assuming valid input) so just return that.
    return stack.pop()


print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
