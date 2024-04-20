def inorderTraversal(self, root):
    res = []

    def rec(node):
        if node:
            rec(node.left)
            res.append(node.val)
            rec(node.right)

    rec(root)
    return res