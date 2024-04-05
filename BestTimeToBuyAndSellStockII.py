def maxProfit(prices):
    total = 0
    curr_buy = prices[0]
    for i in range(1, len(prices)):

        # sell stock at max
        if prices[i] < prices[i - 1]:
            total += prices[i - 1] - curr_buy
            curr_buy = prices[i]

        # buy stock at min
        curr_buy = min(prices[i], curr_buy)

    # This is for when the stock keeps increasing until the end,
    # we never have a chance to sell because no maxima is encountered
    if curr_buy < prices[-1]:
        total += prices[-1] - curr_buy

    return total


def maxProfitDP(prices):
    total = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            total += diff
    return total

