from collections import defaultdict


def count_palindromic_subsequences(s):
    # Track character occurrences infront of and behind current element
    infront = [0] * 26
    behind = [0] * 26
    palindromes = set()

    # Populate infront (Nothing behind the first character
    for c in s:
        infront[ord(c) - ord('a')] += 1

    # Now, check for _c_ pairings in for each character
    for c in s:
        infront[ord(c) - ord('a')] -= 1
        for alphabet in range(0, 26):
            if infront[alphabet] > 0 and behind[alphabet] > 0:
                palindromes.add(chr(ord('a') + alphabet) + c + chr(ord('a') + alphabet))

        behind[ord(c) - ord('a')] += 1
    return len(palindromes)


def count_palindromic_subsequences2(s):
    index_dict = defaultdict(list)  #default values is empty list if key doesnt exist
    for i, char in enumerate(s):
        index_dict[char].append(i)

    res = 0
    for char, indices in index_dict.items():
        if len(indices) < 2:
            continue

        left = indices[0]
        right = indices[-1]
        res += len(set(s[left+1:right]))
    return res


def count_palindromic_subsequences3(s):
    count = 0
    for c in set(s):
        left, right = s.find(c), s.rfind(c)
        count += len(set(s[left+1:right]))
    return count


print(count_palindromic_subsequences3('aabca'))
print(count_palindromic_subsequences3('bbcbaba'))
print(count_palindromic_subsequences3(''))
print(count_palindromic_subsequences3('abc'))
