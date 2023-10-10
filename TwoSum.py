def two_sum1(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]

    return False


def two_sum2(nums, target):
    """ key: diff, value: index """
    table = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]

        if nums[i] in table:
            return [table[nums[i]], nums[i]]

        table[diff] = nums[i]


def two_sum_two_pointer(nums, target):
    left = 0
    right = len(nums) - 1

    # sort array, O(n log n)
    nums.sort()

    while left < right:
        summ = nums[left] + nums[right]
        if summ > target:
            right -= 1
        elif summ < target:
            left += 1
        else:  # sum == target:
            return [nums[left], nums[right]]
    return None


print(two_sum2([2, 7, 11, 15], 9))
print(two_sum2([3, 2, 4], 6))
print(two_sum2([3, 3], 6))
