def is_sub_tree(root, subRoot):
    def same_tree(root_node, sub_node):
        if root_node is None and sub_node is None:
            return True
        if root_node is None or sub_node is None or root_node.val != sub_node.val:
            return False
        return same_tree(root_node.left, sub_node.left) and same_tree(root_node.right, sub_node.right)

    def find_nodes(node):
        if node is None:
            return False
        if node.val == subRoot.val:
            if same_tree(node, subRoot):
                return True
        return find_nodes(node.left) or find_nodes(node.right)
    return find_nodes(root)

