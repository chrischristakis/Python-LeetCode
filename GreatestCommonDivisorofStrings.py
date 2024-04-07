def gcdOfStrings(str1, str2):
    if (str1 + str2) != (str2 + str1):
        return ''

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    return str1[:gcd(len(str1), len(str2))]