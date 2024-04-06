def minRemoveToMakeValid(s):
    open_par = []  # tracks indices of open parentheses
    split = list(s)
    for i, c in enumerate(split):
        if c == '(':
            open_par.append(i)
        if c == ')':
            if open_par:  # resolve an open parenthesis
                open_par.pop()
            else:  # can't 'afford' closing parenthesis, remove it froms string
                split[i] = ''

    # remove unresolved open parenthesis
    while open_par:
        top = open_par.pop()
        split[top] = ''

    return ''.join(split)
