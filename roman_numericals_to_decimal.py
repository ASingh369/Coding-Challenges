"""
Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.

Example:
Input: IX
Output: 9

Input: VII
Output: 7

Input: MCMIV
Output: 1904
Roman numerals are based on the following symbols:
I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000
Numbers are strings of these symbols in descending order. In some cases, subtractive notation is used to avoid repeated characters. The rules are as follows:
1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).
"""

class Solution():
  def romanToInt(self, s):
    result = 0
    last_index = len(s)-1
    skip_next = False
    for i, symbol in enumerate(s):
      if skip_next:
        skip_next = False
        continue
      if symbol is 'I':
        if i < last_index:
          if s[i+1] is 'V':
            result = result + 4
            skip_next = True
          elif s[i+1] is 'X':
            result = result + 9
            skip_next = True
          else:
            result = result + 1
        else:
          result = result + 1
          
      if symbol is 'X':
        if i < last_index:
          if s[i+1] is 'L':
            result = result + 40
            skip_next = True
          elif s[i+1] is 'C':
            result = result + 90
            skip_next = True
          else:
            result = result + 10
        else:
          result = result + 10
          
          
      if symbol is 'C':
        if i < last_index:
          if s[i+1] is 'D':
            result = result + 400
            skip_next = True
          elif s[i+1] is 'M':
            result = result + 900
            skip_next = True
          else:
            result = result + 100
        else:
          result = result + 100

      if symbol is 'V':
        result = result + 5
      elif symbol is 'L':
        result = result + 50
      elif symbol is 'D':
        result = result + 500
      elif symbol is 'M':
        result = result + 1000

    return result
      
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910
