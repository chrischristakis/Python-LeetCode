def is_balanced(root):
    is_balanced.balanced = True

    def inner(node):
        if node is None:
            return 0
        left_depth = inner(node.left) + 1
        right_depth = inner(node.right) + 1
        balance_factor = abs(left_depth - right_depth)
        if balance_factor > 1:
            is_balanced.balanced = False
        return max(left_depth, right_depth)

    inner(root)
    return is_balanced.balanced