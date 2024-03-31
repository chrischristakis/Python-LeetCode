def isHappy(n):
    cache = {}
    while n != 1:
        if n in cache:
            return False
        sum = 0
        digits = n
        while digits > 0:
            sum += (digits % 10)**2
            digits //= 10
        cache[n] = sum
        n = sum
    return True


print(isHappy(19))
print(isHappy(2))
