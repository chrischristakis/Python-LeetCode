def single_number(nums):
    res = 0
    for n in nums:
        # a ^ b == b ^ a, a ^ a = 0, and XOR is associative. So we will end up with our number.
        res ^= n
    return res


print(single_number([4,1,2,1,2]))
