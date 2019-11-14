"""
Given two strings, find if there is a one-to-one mapping of characters between the two strings.

Example
Input: abc, def
Output: True # a -> d, b -> e, c -> f

Input: aab, def
Ouput: False # a can't map to d and e 
"""

def has_character_map(str1, str2):
  # Fill this in.
  if len(str1) != len(str2):
    return False

  map_dict = {}

  for i in range(len(str1)):
    if str1[i] in map_dict:
      if not map_dict[str1[i]] == str2[i]:
        return False
    else:
      map_dict[str1[i]] = str2[i]
  return True

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False