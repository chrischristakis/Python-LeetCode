def three_sum(nums):
    nums.sort()
    res = set()

    for i in range(0, len(nums)):
        # skip if we're looking at a duplicate (since its sorted)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # we don't need to compare elements before our currently selected element, since we've already compared those
        left = i + 1
        right = len(nums) - 1
        while left < right:

            sum = nums[left] + nums[right] + nums[i]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                res.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                left += 1

    return list(res)


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([-1, 0, 1, 0]))
