def rotate(nums, k):
    k %= len(nums)
    if k == 0:
        return nums

    def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    # if k = 3, this is the reuslt we want:
    # input : ---->-->   (represent arr as arrows, smaller portion is the k=3 rotated segment)
    # result: -->---->

    # turn ---->--> into <--<----
    reverse(nums, 0, len(nums) - 1)

    # turn <--<---- into --><----
    reverse(nums, 0, k - 1)

    # turn --><---- into -->---->
    reverse(nums, k, len(nums) - 1)


nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)
