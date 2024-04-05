def minAreaRect(points):
    map = {}

    # Store x as key and y values in set in map
    for x, y in points:
        if x not in map:
            map[x] = set()
        map[x].add(y)

    min_area = float('inf')

    # can skip point pairs we already checked by
    # just iterating through everything after 'i'.
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            Ax, Ay = points[i]
            Bx, By = points[j]

            if Ax == Bx or Ay == By:
                continue  # not diagonal points! Share one axis...

            # check if (Ax, By) and (Bx, Ay) exist to form rectangle w/ diagonal points
            if By in map[Ax] and Ay in map[Bx]:
                length = abs(Ax - Bx)
                width = abs(Ay - By)
                min_area = min(min_area, length * width)

    return min_area if min_area != float('inf') else 0