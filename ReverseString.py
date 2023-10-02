# naive solution
def reverse_string(n):
    result = []
    last_index = len(n) - 1
    # Loop from the last index until 0
    for i in range(0, len(n)):
        result.append(n[last_index-i])

    return ''.join(result)


def reverse_string1(s):
    s = list(s)
    low = 0
    high = len(s) - 1

    while low < high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1

    return ''.join(s)


def reverse_string2(s):
    s[:] = s[::-1]
    return ''.join(s)


print(reverse_string('this is my string'))
print(reverse_string1('this is my string'))
print(reverse_string2('this is my string'))
