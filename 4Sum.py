def fourSum(self, nums, target):
    # process all pairs i, j, then use two pointer on sorted list.
    # we're tracking distinct, so skip when a pointer is pointing to the same number after a move.

    ans = []
    nums.sort()  # O(n log n)
    for i in range(0, len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            # keep moving until we're considering a new number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[j] + nums[left] + nums[right]

                if summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
                else:  # found target
                    ans.append([nums[i], nums[j], nums[left], nums[right]])

                    # move both pointers inwards
                    left += 1
                    right -= 1

                    # keep moving until we're considering a new number
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while right > left and nums[right] == nums[right + 1]: right -= 1
    return ans