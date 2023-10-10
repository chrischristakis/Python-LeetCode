class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        reverse = []
        while len(self.queue) != 0:
            reverse.append(self.queue.pop())

        popped = reverse.pop()
        while len(reverse) != 0:
            self.queue.append(reverse.pop())
        return popped

    def peek(self):
        reverse = []
        while len(self.queue) != 0:
            reverse.append(self.queue.pop())

        peeked = reverse[-1]  # no peek, but if there was a stack we could just use .peek() here
        while len(reverse) != 0:
            self.queue.append(reverse.pop())
        return peeked

    def empty(self):
        return not bool(self.queue)

    def __repr__(self):
        return "FRONT -> " + str(self.queue) + " <- BACK"


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj)
print(obj.peek())
obj.pop()

