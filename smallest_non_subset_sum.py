"""
Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.

Example:
Input: [1, 2, 3, 8, 9, 10]
Output: 7
Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.
"""

def find_smallest(nums):
  if len(nums) <= 0 or nums[0] > 1:
    return 1
  prev_max_sum = 0
  for i in range(1, len(nums)):
    prev_max_sum = 0
    for j in range(i):
      prev_max_sum = prev_max_sum + nums[j]
    if prev_max_sum < nums[i]-1:
      return prev_max_sum+1
  return prev_max_sum+nums[len(nums)-1]+1

  

print(find_smallest([1, 2, 3, 8, 9, 10]))
# 7
print(find_smallest([1, 3, 6, 10, 11, 15]))
print(find_smallest([1, 1, 1, 1]))
print(find_smallest([1, 1, 3, 4]))
print(find_smallest([1, 2, 5, 10, 20, 40]))
print(find_smallest([1, 2, 3, 4, 5, 6]))
print(find_smallest([3]))
print(find_smallest([1]))
print(find_smallest([]))