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


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))

