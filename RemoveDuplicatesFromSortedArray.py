# Bad solution. O(n log n) and space O(n)
def remove_dupes(nums):
    table = {}
    k = 0
    for i in range(0, len(nums)):
        if nums[i] in table:
            table[nums[i]].append(i)
        else:
            k += 1
            table[nums[i]] = [i]

    for indices in table.values():
        print(indices)
        if len(indices) > 1:
            for i in range(1, len(indices)):
                nums[indices[i]] = 999

    nums.sort()
    return k


# Good solution, O(n) and space O(1)
def remove_dupes1(nums):
    k = 0
    last_unique = None
    last_unique_index = -1
    for i in range(0, len(nums)):
        if nums[i] != last_unique:
            last_unique = nums[i]
            nums[last_unique_index + 1], nums[i] = nums[i], nums[last_unique_index + 1]
            last_unique_index += 1
            k += 1

    return k


print(remove_dupes1([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
