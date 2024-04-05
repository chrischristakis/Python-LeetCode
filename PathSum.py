def hasPathSum(root, targetSum):
    if root is None:
        return False

    found = False

    def dfs(node, sum=0):
        if node.left is None and node.right is None:
            if sum + node.val == targetSum:
                found = True
            return
        if node.left:
            dfs(node.left, sum + node.val)
        if node.right:
            dfs(node.right, sum + node.val)

    dfs(root)
    return found
