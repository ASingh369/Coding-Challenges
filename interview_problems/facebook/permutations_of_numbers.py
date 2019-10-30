"""
You are given an array of integers. Return all the permutations of this array.

"""

def permute_helper(nums, start):
    if start == len(nums)-1:
        x.append(nums)
    else:
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            permute_helper(nums, start+1)
            nums[start], nums[i] = nums[i], nums[start]


def permute(nums):
    global x
    x = []
    permute_helper(nums, 0)
    return x
  

print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]