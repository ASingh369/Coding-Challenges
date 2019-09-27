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

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def are_mirror(root1, root2):
  if root1.value != root2.value:
    return False
  if len(root1.children) != len(root2.children):
    return False
  
  for i in range(len(root1.children)):
    if not are_mirror(root1.children[i], root2.children[len(root1.children)-i-1]):
      return False

  return True

def is_symmetric(root):
  if len(root.children) != 2:
    return False
  return are_mirror(root.children[0], root.children[1])

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True