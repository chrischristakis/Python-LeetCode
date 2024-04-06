def findPeakElement(nums):
    min = 0
    max = len(nums) - 1

    while min <= max:
        guess = (min + max) // 2
        e = nums[guess]
        left = float('-inf') if guess < 1 else nums[guess - 1]
        right = float('-inf') if guess > len(nums) - 2 else nums[guess + 1]
        if e > left and e > right:
            return guess
        elif e < left:
            max = guess - 1
        else:
            min = guess + 1