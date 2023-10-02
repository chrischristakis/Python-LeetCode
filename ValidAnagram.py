def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    s_table = {}
    for e in s:
        if e in s_table:
            s_table[e] += 1
        else:
            s_table[e] = 1

    t_table = {}
    for e in t:
        if e in t_table:
            t_table[e] += 1
        else:
            t_table[e] = 1

    return s_table == t_table


def valid_anagram1(s, t):
    if len(s) != len(t):
        return False

    alphabet = [0]*26  # O(1)
    for e in s:
        alphabet[ord('a') - ord(e)] += 1
    for e in t:
        alphabet[ord('a') - ord(e)] -= 1

    for e in alphabet:
        if e != 0:
            return False
    return True


print(valid_anagram('rat', 'car'))  # false
print(valid_anagram('angarma', 'anagram'))  # true
