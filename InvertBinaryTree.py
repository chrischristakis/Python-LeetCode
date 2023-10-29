class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        def inner(node):
            if node is None:
                return 'null'
            return '({0}: left:{1}, right:{2})'.format(node.val, inner(node.left), inner(node.right))
        return inner(self)


def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


roott = TreeNode(4)
roott.left = TreeNode(2)
roott.left.left = TreeNode(1)
roott.left.right = TreeNode(3)
roott.right = TreeNode(7)
roott.right.left = TreeNode(6)
roott.right.right = TreeNode(9)

print(roott)
invert_tree(roott)
print(roott)
