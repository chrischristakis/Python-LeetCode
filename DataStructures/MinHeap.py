class MinHeap:
    def __init__(self, arr):
        self.heap = arr
        self.build()

    def build(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.heapify_down(i)

    def lookup(self, val):
        for i in range(0, len(self.heap)):
            if self.heap[i] == val:
                return i
        return -1

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def delete(self, val):
        found = self.lookup(val)
        if found == -1:
            return

        # If element is the last leaf, we can just remove it and we're done.
        last_index = len(self.heap) - 1
        if found == last_index:
            self.heap.pop()
            return

        # Otherwise, we swap with the last leaf, delete the new last leaf, and heapify down from there.
        self.heap[found], self.heap[last_index] = self.heap[last_index], self.heap[found]
        self.heap.pop()
        self.heapify_down(found)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        min = self.heap.pop()
        self.heapify_down(0)
        return min

    # index: what index to start heapifying at
    def heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = left_index + 1

        # No left child means this is a leaf node (A right child will always have a left child since completed tree)
        if left_index >= len(self.heap):
            return

        val = self.heap[index]
        left = self.heap[left_index]
        right = self.heap[right_index] if right_index < len(self.heap) else float('+inf')

        # Swap with smaller child
        smallest_val, smallest_index = (left, left_index) if left < right else (right, right_index)

        if val > smallest_val:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self.heapify_down(smallest_index)

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return

        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def __repr__(self):
        return str(self.heap)


minheap = MinHeap([7,6,5,4,3,2])
print(minheap)  # [2, 3, 5, 4, 6, 7]
minheap.delete(3)
print(minheap)  # [2, 4, 5, 7, 6]
minheap.extract_min()  # 2
print(minheap)  # [4, 6, 5, 7]
minheap.insert(1)
print(minheap)  # [1, 4, 5, 7, 6]
