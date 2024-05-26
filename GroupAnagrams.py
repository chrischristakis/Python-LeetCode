def group_anagrams(strs):
    sorted_table = {}
    for i in range(0, len(strs)):
        sorted_str = ''.join(sorted(strs[i]))
        if sorted_str in sorted_table:
            sorted_table[sorted_str].append(strs[i])
        else:
            sorted_table[sorted_str] = [strs[i]]

    res = []
    for key, words in sorted_table.items():
        res.append(words)
    return res

def better_anagrams(strs):
    res = {}
    for s in strs:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1

        key = tuple(counter)  # counter becomes immutable, thus hashable
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]
    return res.values()


print(better_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(better_anagrams([""]))

