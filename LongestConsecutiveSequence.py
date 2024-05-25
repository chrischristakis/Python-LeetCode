#O(n log n)
def longestConsecutive1(nums):
    if not nums:
        return 0
    nums = list(set(nums))
    nums.sort()
    longest = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr += 1
            longest = max(longest, curr)
        else:
            curr = 1
    return longest

def longestConsecutive2(nums):
    s = set(nums)
    longest = 0
    for n in s:
        if n - 1 not in s:
            offset = 1
            while n + offset in s:
                offset += 1
            longest = max(longest, offset)
    return longest