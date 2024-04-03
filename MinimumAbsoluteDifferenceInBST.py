def getMinimumDifference(root):
    min_abs = float('inf')
    prev = None

    def search(node):
        nonlocal prev, min_abs
        if node is None:
            return

        # in order
        # left
        if node.left:
            search(node.left)

        # current node, use previously visited node (bst + inorder = sorted!)
        if prev is not None:
            min_abs = min(min_abs, node.val - prev)

        prev = node.val

        # right
        if node.right:
            search(node.right)

    search(root)
    return min_abs
