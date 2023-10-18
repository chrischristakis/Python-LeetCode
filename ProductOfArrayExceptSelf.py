def product_except_self(nums):
    # Calculate prefix array by multiply elements together
    prefix = []
    for i in range(0, len(nums)):
        if i == 0:
            prefix.append(nums[i])
            continue
        prefix.append(prefix[i-1] * nums[i])

    # Post fix is the same as prefix, but we do things from right to left.
    postfix = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            postfix[i] = nums[i]
            continue
        postfix[i] = postfix[i + 1] * nums[i]

    # Now that we have our lists, we can determine the product to the left (prefix) or right (postfix) of the element
    res = []
    for i in range(0, len(nums)):

        # Edges of array should just use 1 (the no effect on product)
        left = 1 if i == 0 else prefix[i-1]
        right = 1 if i == (len(nums) - 1) else postfix[i + 1]

        res.append(left * right)

    return res


print(product_except_self([1, 5, 3, 2, 4]))
