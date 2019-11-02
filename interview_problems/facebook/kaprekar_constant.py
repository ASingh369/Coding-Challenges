"""

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