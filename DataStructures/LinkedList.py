class Node:
    def __init__(self, val=0, next_node=None):
        self.next_node = next_node
        self.val = val


# Singly linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, val):
        new_node = Node(val)
        if self.count == 0:
            self.head = new_node
        else:
            curr = self.head
            while curr.next_node is not None:
                curr = curr.next_node
            curr.next_node = new_node

        self.count += 1

    def prepend(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        self.count += 1

    def delete(self, index):
        if index < 0 or index >= self.count or self.count == 0:
            return

        prev = None
        curr = self.head
        for i in range(1, index + 1):
            prev = curr
            curr = curr.next_node

        if curr == self.head:
            self.head = curr.next_node
        else:
            prev.next_node = curr.next_node

        self.count -= 1

    def __repr__(self):
        curr = self.head
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.next_node
        return str(res)


if __name__ == '__main__':
    singly = LinkedList()

    singly.prepend(4)
    singly.prepend(5)
    singly.append(2)

    print(singly)  # [5, 4, 2]

    singly.delete(1)

    print(singly)  # [5, 2]
