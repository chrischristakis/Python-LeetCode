# Worse solution, TLE
def canJumpDP(nums):
    dp = [False] * len(nums)
    dp[0] = True
    for i in range(len(nums) - 1):
        for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
            dp[j] = dp[i]
    return dp[-1]


# Greedy, best solution
def canJump(nums):
    max_index = 0
    i = 0
    while i <= max_index:
        max_index = max(max_index, i + nums[i])
        if max_index >= len(nums) - 1:
            return True
        i += 1

    return False


print(canJump([0, 2, 3]))
