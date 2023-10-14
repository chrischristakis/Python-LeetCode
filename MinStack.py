class Node:
    def __init__(self, val=0, min=float('inf'), next=None):
        self.val = val
        self.next = next
        self.min = min


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val, val)
        else:
            self.head = Node(val, min(val, self.head.min), self.head)

    def pop(self):
        self.head = self.head.next

    def top(self):
        return self.head.val

    def get_min(self):
        return self.head.min

    def __repr__(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return str(res)


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack)
print(minStack.get_min())  # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.get_min())  # return -2
