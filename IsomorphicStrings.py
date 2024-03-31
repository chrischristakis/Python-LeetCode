def isIsomorphic(s, t):
    # len(s) == len(t), can use one pointer for both
    mappings = {}
    used = set()
    for i in range(len(s)):
        sc = s[i]
        tc = t[i]

        if sc not in mappings:
            if tc in used:
                return False
            used.add(tc)
            mappings[sc] = tc
        else:
            if mappings[sc] != tc:
                return False
    return True
