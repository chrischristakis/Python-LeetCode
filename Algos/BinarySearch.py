def iter_bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        val = arr[middle]

        if val > target:
            right = middle - 1
        elif val < target:
            left = middle + 1
        else:
            return True

    return False


def recursive_bin_search(arr, target):
    def inner(left, right):
        if left > right:
            return False

        middle = left + (right - left) // 2
        val = arr[middle]

        if val > target:
            return inner(left, middle - 1)
        elif val < target:
            return inner(middle + 1, right)
        else:
            return True

    return inner(0, len(arr) - 1)


print(recursive_bin_search([3, 5, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20, 22, 23, 25, 28, 29,
                  30, 37, 38, 40, 41, 42, 44, 45, 50, 51, 52, 53, 56, 57, 58, 59,
                  60, 66, 70, 76, 77, 81, 82, 83, 84, 85, 89, 90, 91, 92, 96, 98,
                  99, 100, 110, 130, 131, 135, 190, 201, 215, 219, 256, 257, 300],

                  13))
