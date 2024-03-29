def gcd(a, b):
    while b != 0:
        if a > b:  # make sure B >= A
            a, b = b, a
        b %= a
    return a

print(gcd(7, 7))
print(gcd(7, 5))
print(gcd(15, 21))