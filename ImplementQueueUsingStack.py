class Queue:
    def __init__(self):
        self.queue = []  # stack

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        reverse = []
        while len(self.queue) != 0:
            reverse.append(self.queue.pop())
        front = reverse.pop()
        while len(reverse) != 0:
            self.queue.append(reverse.pop())
        return front

    def __repr__(self):
        return str(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue)
