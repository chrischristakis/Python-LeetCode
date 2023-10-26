def climbing_stairs(n):
    def recur(sum):
        if sum > n:
            return 0  # We went beyond the steps
        elif sum == n:
            return 1  # Valid solution
        else:
            return recur(sum + 1) + recur(sum + 2)

    return recur(0)


def memo_climbing_stairs(n):
    cache = {}

    def recur(sum):
        if sum in cache:
            return cache[sum]

        if sum > n:
            return 0
        elif sum == n:
            return 1
        else:
            distinct = recur(sum + 1) + recur(sum + 2)
            cache[sum] = distinct
            return distinct

    return recur(0)


def dp_climbing_stairs(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # dp[i] is the distinct ways to reach the i'th step

    # Base cases, step 1 and 2 can be reached from the beginning.
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # i-1 would append 1 step to get new paths to i'th stair, i-2 would append 2 steps.
    return dp[n]


def space_dp_climbing_stairs(n):
    if n == 1 or n == 2:
        return n

    one_behind = 2
    two_behind = 1
    curr = one_behind + two_behind

    for i in range(3, n + 1):
        curr = one_behind + two_behind
        two_behind = one_behind
        one_behind = curr
    return curr


print(memo_climbing_stairs(35))
print(dp_climbing_stairs(35))
print(space_dp_climbing_stairs(35))
