"""
Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit 
number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

This certain function is as follows:
- Order the number in ascending form and descending form to create 2 numbers.
- Pad the descending number with zeros until it is 4 digits in length.
- Subtract the ascending number from the descending number.
- Repeat.

Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant.
"""

KAPREKAR_CONSTANT = 6174


def sort_ascending(n):
  n = ''.join(sorted(str(n)))
  return int(n)

def sort_descending(n):
  n = ''.join(sorted(str(n)))[::-1]
  if len(n) < 4:
    for i in range(len(n), 4):
      n = n + '0'
  return int(n)


def number_kaprekar_iterations(n, count=1):
  ascending = sort_ascending(n)
  descending = sort_descending(n)
  diff = descending - ascending
  if diff == KAPREKAR_CONSTANT:
    return count
  return number_kaprekar_iterations(diff, count+1)

print(number_kaprekar_iterations(123))