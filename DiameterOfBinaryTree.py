class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root):
    diameter.max_length = 0

    def inner(node):
        left_longest = inner(node.left) + 1 if node.left else 0
        right_longest = inner(node.right) + 1 if node.right else 0

        diameter.max_length = max(left_longest + right_longest, diameter.max_length)

        return max(left_longest, right_longest)

    inner(root)
    return diameter.max_length


roott = TreeNode(1)
roott.left = TreeNode(2)
roott.right = TreeNode(3)
roott.left.left = TreeNode(4)
roott.left.right = TreeNode(5)
roott.left.left.left = TreeNode(6)
roott.left.right.right = TreeNode(7)
roott.left.right.right.left = TreeNode(8)
roott.left.right.right.right = TreeNode(9)

print(diameter(roott))
