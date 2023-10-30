class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0

    def inner(node, depth):
        if node is None:
            return depth
        return max(inner(node.left, depth + 1), inner(node.right, depth + 1))
    return inner(root, 0)


roott = TreeNode(3)
roott.left = TreeNode(9)
roott.right = TreeNode(20)
roott.right.left = TreeNode(15)
roott.right.right = TreeNode(7)

print(max_depth(roott))
