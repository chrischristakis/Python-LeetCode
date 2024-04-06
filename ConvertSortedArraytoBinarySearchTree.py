class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    # simple Binary search for middle element (always from 0-len(nums))
    mid = len(nums) // 2

    # since bsts are in order (left, parent, right) we know the root will be in the middle
    # of the array and can keep doing this for the subarrays, repeating.
    return TreeNode(
        nums[mid],
        self.sortedArrayToBST(nums[:mid]),  # left subtree
        self.sortedArrayToBST(nums[mid + 1:])  # right subtree
    )

