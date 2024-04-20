def summaryRanges(nums):
    if len(nums) == 0:
        return nums

    start = end = nums[0]
    res = []
    for n in nums[1:]:
        if n != (end + 1):
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            start = n
        end = n

    # for remainder
    if start == end:
        res.append(str(start))
    else:
        res.append(str(start) + "->" + str(end))

    return res
