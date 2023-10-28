def word_break(s, word_dict):
    cache = set()

    def inner(st):
        if len(st) == 0:
            return True
        if st in cache:
            return False
        for word in word_dict:
            # our string can't contain a word bigger than itself
            if len(word) > len(st):
                continue

            if st[0:len(word)] == word:
                if inner(st[len(word):len(st)]):
                    return True
        cache.add(st)
        return False

    return inner(s)


def dp_word_break(s, word_dict):
    dp = [False] * (len(s) + 1)  # Our dp array stores if there is a valid substring at index i

    # Base case is element after string, chain it to the front for input to be successful!
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:
            if i + len(word) <= len(s):
                if s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
    return dp[0]


func = dp_word_break
print(func("applepenapple", ["apple","pen"]))
print(func("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
