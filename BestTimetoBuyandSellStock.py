def bf_max_profit(prices):
    max_profit = -1
    for i in range(0, len(prices)):
        curr_max = prices[i]
        for j in range(i+1, len(prices)):
            curr_max = max(curr_max, prices[j])
        max_profit = max(curr_max - prices[i], max_profit)
    return max_profit


def dp_max_profit(prices):
    curr_min = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < curr_min:
            curr_min = price
        max_profit = max(price - curr_min, max_profit)
    return max_profit


# Optimized version of what's above, only compare when necessary. Allows us to skip some iterations,
# but don't worry about this one much.
def dpp_max_profit(prices):
    lowest = highest = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price > highest:
            highest = price
        if price < lowest:
            max_profit = max(highest - lowest, max_profit)
            lowest = highest = price
    return max(highest - lowest, max_profit)


soln = dpp_max_profit
print(soln([7,1,5,3,6,4]))
print(soln([7,6,4,3,1]))
