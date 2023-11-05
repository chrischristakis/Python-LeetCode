def level_order(self, root):
    levels = {}

    def dfs(node, level):
        if node is None:
            return
        if level not in levels:
            levels[level] = []
        levels[level].append(
            node.val
        )
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)
    return levels.values()
