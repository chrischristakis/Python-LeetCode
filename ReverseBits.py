def reverseBits(n):
    ans = 0
    for i in range(32):
        ans |= ((n >> i) & 1) << (31 - i)
    return ans