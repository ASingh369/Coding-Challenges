"""
A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same as the right side of the tree.

Here's an example of a symmetrical k-ary tree.
        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9
Given a k-ary tree, figure out if the tree is symmetrical.
"""

import queue

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
  root_children = len(root.children)
  if root_children is 0:
    return True

  left_queue = queue.Queue()
  right_queue = queue.Queue()

  for i in range(root_children//2):
    left_queue.put(root.children[i]); right_queue.put(root.children[root_children-i-1])

  while left_queue.qsize() > 0 and right_queue.qsize() > 0:
    left = left_queue.get(); right = right_queue.get()
    if left.value != right.value:
      return False
    for child in left.children:
      left_queue.put(child)

    for child in reversed(right.children):
      right_queue.put(child)

  # In case root has odd number of children
  if root_children%2 != 0:
    return is_symmetric(root.children[root_children//2])

  return True

'''
Test Cases
'''
tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True

tree2 = Node(1)
tree2.children = [Node(2), Node(3), Node(2)]
tree2.children[0].children = [Node(9), Node(4), Node(1)]
tree2.children[1].children = [Node(2), Node(2)]
tree2.children[2].children = [Node(1), Node(4), Node(9)]

print(is_symmetric(tree2))

tree3 = Node(3)
print(is_symmetric(tree3))