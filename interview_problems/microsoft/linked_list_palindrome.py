"""
You are given a doubly linked list. Determine if it is a palindrome.
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
  if node == None:
    return True

  current = node
  while current.next != None:
    current = current.next

  start = node
  end = current

  while start != end:
    if start.val != end.val:
      return False
    else:
      if start.next == end:
        if start.next.val == end.val:
          return True
        else:
          return False
      start = start.next
      end = end.prev

  return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True