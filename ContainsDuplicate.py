def contains_duplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate1(nums):
    lut = {}
    for e in nums:
        if e in lut:
            return True
        lut[e] = True
    return False


print(contains_duplicate1([1, 2, 3, 4]))  # false
print(contains_duplicate1([1, 2, 3, 1]))  # true
print(contains_duplicate1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
