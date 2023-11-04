class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


roott = TreeNode(1)
roott.left = TreeNode(2)
roott.right = TreeNode(3)
roott.left.left = TreeNode(4)
roott.left.right = TreeNode(5)
roott.right.left = TreeNode(6)
roott.right.right = TreeNode(7)