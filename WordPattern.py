def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False

    pattern_to_word = {}
    word_to_pattern = {}
    for pat, word in zip(pattern, words):
        if pat in pattern_to_word:
            if pattern_to_word[pat] != word:
                return False
        else:
            if word in word_to_pattern:
                return False
            word_to_pattern[word] = pat
            pattern_to_word[pat] = word
    return True


print(wordPattern("acba", "dog cat cat dog"))

