def min_eating_speed(piles, h):
    min_k = float('+inf')

    def calculate_time(k_option):
        time = 0
        for pile in piles:
            time += math.ceil(float(pile)/k_option)
        return time

    for k in range(1, max(piles) + 1):
        if calculate_time(k) <= h:
            min_k = min(min_k, k)
    return min_k


def min_eating_speed2(piles, h):
    left = 1
    right = max(piles)
    min_k = right  # max of piles will always be a valid option, but hardly ever the optimized one

    def calculate_time(k_option):
        time = 0
        for pile in piles:
            time += pile // k_option
            if pile % k_option != 0:
                time += 1
        return time

    while left <= right:
        k = left + (right - left) // 2
        t = calculate_time(k)
        if t <= h:
            min_k = min(min_k, k)
            right = k - 1
        else:
            left = k + 1

    return min_k


print(min_eating_speed2([30,11,23,4,20], 5))
print(min_eating_speed2([3,6,7,11], 8))
