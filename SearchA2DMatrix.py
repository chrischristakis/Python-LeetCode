def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    # 1D indices
    left = 0
    right = (m * n) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Transform 1D mid index into 2D array indices
        row = mid // n
        col = mid % n
        val = matrix[row][col]

        if val < target:
            left = mid + 1
        elif val > target:
            right = mid - 1
        else:
            return True

    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
