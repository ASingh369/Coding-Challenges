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
    print(root1.value, root2.value)

    return False
  if len(root1.children) != len(root2.children):
    print(2)
    return False
  
  for i in range(len(root1.children)):
    if not are_mirror(root1.children[i], root2.children[len(root1.children)-i-1]):
      print(3)
      return False

  return True

def is_symmetric(root):
  if len(root.children)%2 == 0:
    for i in range(len(root.children)//2):
      if not are_mirror(root.children[i], root.children[len(root.children)-i-1]):
        print(4)
        return False
    return True
  else:
    for i in range(len(root.children)//2):
      if not are_mirror(root.children[i], root.children[len(root.children)-i-1]):
        print(root.value)
        return False
    return is_symmetric(root.children[len(root.children)//2 + 1])

  return are_mirror(root.children[0], root.children[1])

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True

tree2 = Node(1)
tree2.children = [Node(2), Node(3), Node(2)]
tree2.children[0].children = [Node(9), Node(4), Node(1)]
tree2.children[2].children = [Node(1), Node(4), Node(9)]

print(is_symmetric(tree2))