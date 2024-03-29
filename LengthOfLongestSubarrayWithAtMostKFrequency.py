def a(nums, k):
    left = 0
    max_width = 0

    # stores the count of each element, as well at their indices in a queue.
    counter = {}

    for r in range(len(nums)):
        if nums[r] not in counter:
            counter[nums[r]] = 0
        counter[nums[r]] += 1

        while counter[nums[r]] > k:
            counter[nums[left]] -= 1
            left += 1

        max_width = max(max_width, r - left + 1)
    return max_width


print(a([1,2,2,2,4], 1))
