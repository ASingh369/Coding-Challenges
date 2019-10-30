"""
Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
"""

def compareNums(num1, num2):
  ab = str(num1)+str(num2)
  ba = str(num2)+str(num1)
  return int(ab) > int(ba)

def partition(arr, start, end):
  pivot = arr[start]
  
  low = start+1
  high = end
  while high >= low:
    if compareNums(arr[low], pivot):
      low = low + 1
      continue
    elif compareNums(pivot, arr[high]):
      high = high - 1
      continue
    elif compareNums(arr[high], pivot) and compareNums(pivot, arr[low]):
      arr[low], arr[high] = arr[high], arr[low]
      low = low + 1
      high = high - 1

  if low == high:
    arr[start], arr[low] = arr[low], arr[start]
    return low
  else: 
    arr[start], arr[low-1] = arr[low-1], arr[start]
    return low-1


def quickSort(arr, low, high):
  if high > low:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


def largestNum(nums):
  quickSort(nums, 0, len(nums)-1)
  return ''.join(str(e) for e in nums)
  

print(largestNum([17, 7, 2, 45, 72]))
# 77245217

