def containsNearbyDuplicate1(nums, k):
    seen = {}
    for i, e in enumerate(nums):
        if e in seen and i - seen[e] <= k:
            return True
        seen[e] = i
    return False


def containsNearbyDuplicate(nums, k):
    if k == 0:
        return False

    left = 0
    next = min(k, len(nums))
    elems = set()

    # initialize set
    for i in range(next):
        if nums[i] in elems:
            return True
        elems.add(nums[i])

    while next < len(nums):
        if nums[next] in elems:
            return True
        elems.remove(nums[left])
        elems.add(nums[next])

        # move window
        left += 1
        next += 1
    return False


print(containsNearbyDuplicate1([1,2,3], 0))
print(containsNearbyDuplicate1([1,2,3,1,2,3], 2))
