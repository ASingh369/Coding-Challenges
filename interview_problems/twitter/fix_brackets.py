"""
Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.

Example:
Input: '(()()'
Output: 1
Explanation:

The fixed string could either be ()() by deleting the first bracket, or (()()) by adding a bracket. These are not the only ways of fixing the string, there are many other ways by adding it in different positions!

"""

def fix_brackets(s):
  result = 0
  stack = []
  for char in s:
    if char == '(':
      stack.append(char)
    else:
      if len(stack) == 0 or stack.pop() != '(':
        result = result + 1
  
  result = result + len(stack)
  return result


print(fix_brackets('(()()'))
# 1
print(fix_brackets(')(()()))'))