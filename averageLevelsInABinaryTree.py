def averageOfLevelsDFS(root):
    avgs = []

    def dfs(node, depth=0):
        nonlocal avgs
        if node is None:
            return

        if depth > len(avgs) - 1:
            avgs.append([])

        avgs[depth].append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root)

    res = []
    for depths in avgs:
        res.append(float(sum(depths)) / len(depths))
    return res


def averageOfLevelsBFS(root):
    queue = deque([root])
    avgs = []
    while queue:
        sum = 0
        num_of_nodes = len(queue)

        # Len of queue is before we add stuff to it, so things only pertaining
        # to the current level!
        for i in range(len(queue)):
            node = queue.popleft()
            sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        avgs.append(float(sum) / num_of_nodes)
    return avgs