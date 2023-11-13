def character_replacement(s, k):
    max_len = max_freq = 0
    left = 0
    occurrences = {}

    for right in range(len(s)):
        if s[right] not in occurrences:
            occurrences[s[right]] = 1
        else:
            occurrences[s[right]] += 1

        max_freq = max(occurrences[s[right]], max_freq)

        window_length = right - left + 1
        while window_length - max_freq > k:
            occurrences[s[left]] -= 1
            left += 1
            window_length = right - left + 1

        max_len = max(max_len, window_length)

    return max_len


print(character_replacement('ABABBA', 2))