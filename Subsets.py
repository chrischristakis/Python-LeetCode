def subsets(nums):
    res = []
    def bt(i=0, curr=[]):
        if i == len(nums):
            res.append(curr)
        else:
            bt(i+1, curr + [nums[i]])
            bt(i+1, curr)
    bt()
    return res


print(subsets([1,2,3]))
