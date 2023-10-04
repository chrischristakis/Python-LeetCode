def k_entries1(nums, k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Reverse the list so that our keys become our values
    freq_rev = {}
    for key, val in freq.items():
        if val in freq_rev:
            freq_rev[val].append(key)
        else:
            freq_rev[val] = [key]

    # highest possible frequency of a num occurring is the len of the num input itself,
    # so we loop backwards from that until we have our k elements
    res = []
    for i in range(len(nums), -1, -1):
        if i in freq_rev:
            for e in freq_rev[i]:
                res.append(e)
                if len(res) == k:
                    return res

    return res


print(k_entries1([1, 1, 1, 2, 2, 3], 2))
print(k_entries1([4, 1, -1, 2, -1, 2, 3], 2))
print(k_entries1([1], 1))
