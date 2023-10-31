import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = list(nums)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # return 4
print(kthLargest.add(5))  # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))  # return 8
print(kthLargest.add(4))   # return 8
