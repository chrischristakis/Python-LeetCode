def jump_dp(nums):
    dp = [float('inf')] * len(nums)
    dp[0] = 0
    for i, e in enumerate(nums):

        # check if we can reach other steps less steps.
        for j in range(i + 1, min(i + e + 1, len(nums))):
            dp[j] = min(dp[i] + 1, dp[j])

    return dp[-1]


def jump(nums):
    furthest = 0
    last_of_range = 0
    jumps = 0
    for i in range(len(nums) - 1):
        furthest = max(furthest, i + nums[i])

        if i == last_of_range:
            last_of_range = min(furthest, len(nums) - 1)
            jumps += 1

    return jumps
