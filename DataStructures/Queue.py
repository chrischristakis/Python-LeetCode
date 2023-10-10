class Node:
    def __init__(self, val=0, next_node=None):
        self.next_node = next_node
        self.val = val


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, val):
        new_node = Node(val)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return

        popped = self.head
        self.head = self.head.next_node
        self.count -= 1
        return popped.val

    def __repr__(self):
        curr = self.head
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.next_node
        return "HEAD -> " + str(res) + " <- TAIL"


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # HEAD -> [1, 2, 3] <- TAIL
    print('Dequeued: ', queue.dequeue())  # Dequeued: 1
    print('Dequeued: ', queue.dequeue())  # Dequeued: 2
    print(queue)  # HEAD -> [3] <- TAIL
