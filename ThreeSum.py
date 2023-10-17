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


def three_sum2(nums):
    res = set()
    positive = [num for num in nums if num > 0]
    negative = [num for num in nums if num < 0]
    zeroes = [num for num in nums if num == 0]

    # Allows quick indexing which we will use
    pos_set = set(positive)
    neg_set = set(negative)

    # check for (0,0,0)
    if len(zeroes) >= 3:
        res.add((0, 0, 0))

    # Check for (+x, 0, -x) (note: we can parse either pos_set or neg_set to find symmetric elements)
    if len(zeroes) > 0:
        for pos in pos_set:
            if (pos * -1) in neg_set:
                res.add((pos, 0, pos * -1))

    # for all positive pairs, find negative symmetric to their sum
    for i in range(len(positive)):
        for j in range(i+1, len(positive)):  # We don't need to iterate previous elements, since already checked.
            sum = positive[i] + positive[j]
            if sum * -1 in neg_set:
                res.add(tuple(sorted((positive[i], positive[j], sum * -1))))  # Sorted to remove duplicates

    # Same for negative pairs
    for i in range(len(negative)):
        for j in range(i+1, len(negative)):
            sum = negative[i] + negative[j]
            if sum * -1 in pos_set:
                res.add(tuple(sorted((negative[i], negative[j], sum * -1))))

    return list(res)


print(three_sum2([-1, 0, 1, 2, -1, -4]))
print(three_sum2([-1, 0, 1, 0]))
