def merge(intervals):

    # sort based off first value in interval
    intervals.sort(key=lambda interval: interval[0])

    # if i1 overlaps with i2
    def overlaps(i1, i2):
        return (i1[0] <= i2[1]) and (i1[1] >= i2[0])

    def merge(i1, i2):
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    merged_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        merged = merged_intervals[-1]

        if overlaps(merged, interval):
            merged_intervals[-1] = merge(merged, interval)
        else:
            merged_intervals.append(interval)
    return merged_intervals
