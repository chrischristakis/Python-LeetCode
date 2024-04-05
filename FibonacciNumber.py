def fibonacci(n):
    cache = {}

    def inner(fib_n):
        if fib_n == 0 or fib_n == 1:
            return fib_n
        if fib_n in cache:
            return cache[fib_n]
        res = inner(fib_n - 1) + inner(fib_n - 2)
        cache[fib_n] = res
        return res

    return inner(n)


def iter_fib(n):
    if n == 0 or n == 1:
        return n
    prev1 = 1
    prev2 = 0
    curr = prev1 + prev2
    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr


print(fibonacci(100))


for i in range(2, 3):
    print(i)