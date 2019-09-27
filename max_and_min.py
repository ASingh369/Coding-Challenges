"""
Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.
"""

def find_min_max(nums):
  if len(nums) == 1:
    return {"min": nums[0], 'max': nums[0]}
  
  if nums[0] > nums[1]:
    max = nums[0]; min = nums[1]
  else:
    min = nums[0]; max = nums[1]
  
  for i in range(2, len(nums)):
    if nums[i] > max:
      max = nums[i]
    elif nums[i] < min:
      min = nums[i]

  return {"min": min, "max": max} 

print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)