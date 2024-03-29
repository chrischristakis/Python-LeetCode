def isSubsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return len(s) == 0

    sptr = 0
    tptr = 0
    while tptr < len(t) and sptr < len(s):
        c = t[tptr]
        if s[sptr] == c:
            sptr += 1
        tptr += 1
    return sptr == len(s)
