def kthFactor(n, k):
    left = []
    right = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            left.append(i)
            right.append(n // i)
    if left[-1] == right[-1]:
        right.pop()

    factors = left + right[::-1]
    return factors[k - 1] if k <= len(factors) else -1