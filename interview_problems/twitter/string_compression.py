"""
Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
"""

class Solution(object):
  def compress(self, chars):
    compressed = []
    index = 0
    while index < len(chars):
      current_char = chars[index]
      count = 1
      compressed.append(current_char)
      
      while index+1 < len(chars) and chars[index+1] == current_char:
        index = index + 1
        count = count + 1

      if count > 1:
        compressed.append(count)

      index = index + 1

    return compressed
      
print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']