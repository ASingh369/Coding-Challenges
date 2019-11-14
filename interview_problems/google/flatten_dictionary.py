"""
Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
You can assume there will be no arrays, and all keys will be strings.
"""

import queue

def flatten_dictionary(d, base=''):
  flat_dict = {}
  
  for key in d:
    new_key = base + '.' + key if base else key
    if isinstance(d[key], dict):
      flat_dict.update(flatten_dictionary(d[key], new_key))
    else:
      flat_dict[new_key] = d[key]
  return flat_dict
  

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}