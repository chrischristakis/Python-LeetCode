def longest_substring(s):
    longest = 0
    for i in range(0, len(s)):
        unique = set()
        length = 0
        for j in range(i, len(s)):
            if s[j] in unique:
                break
            unique.add(s[j])
            length += 1
        longest = max(longest, length)
    return longest


def tp_longest_substring(s):
    longest = 0
    left = 0
    chars = {}  # holds (character: index)
    for right in range(len(s)):
        if s[right] in chars and chars[s[right]] >= left:
            left = chars[s[right]] + 1  # left moves to the index of the repeating char + 1
        else:
            # + 1 since imagine 'ab', right = 1, left = 0 is a string of length 2, even though right - left = 1
            longest = max(right - left + 1, longest)
        chars[s[right]] = right
    return longest


func = tp_longest_substring
print(func('abcabcbb'))
print(func('tmmzuxt'))
print(func(' '))
