def hIndex(citations):
    citations.sort()
    h = 0
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] > h:
            h += 1
        else:
            break
    return h