class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        curr = self.root
        while curr:
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    break
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = Node(val)
                    break
                curr = curr.right
            else:
                break  # value exists already

    def lookup(self, val):
        if not self.root:
            return None

        curr = self.root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None

    def __repr__(self):
        def inner(node):
            if not node:
                return 'None'
            left = inner(node.left)
            right = inner(node.right)
            return '({0}: left:{1}, right:{2})'.format(node.val, left, right)
        return inner(self.root)


bst = BST()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.lookup(15))
