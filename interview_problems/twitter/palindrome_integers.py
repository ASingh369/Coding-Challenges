"""
Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.
"""

import math

def is_palindrome(n):
  copy_n = n
  reverse_n = 0


  while copy_n > 0:
    reverse_n = reverse_n * 10 + (copy_n % 10)
    copy_n = copy_n // 10

  if reverse_n == n:
    return True
  return False


print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False