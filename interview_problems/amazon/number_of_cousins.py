"""
Given a binary tree and a given node value, return all of the node's cousins. Two nodes are considered cousins if 
they are on the same level of the tree with different parents. You can assume that all nodes will have their own 
unique value.
"""

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):

  def get_level(self, root, val, level):
    if root == None:
      return
    if root.value == val:
      return level
    else:
      _level = self.get_level(root.left, val, level+1)
      if _level == None:
        _level = self.get_level(root.right, val, level+1)
      return _level

  def print_level_cousins(self, tree, val, level):
    if (tree == None or level < 2):  
        return
  
    if (level == 2): 
        if (tree.left == val or
            tree.right == val):  
            return
        if (tree.left):  
            print(tree.left.value, end = " ")  
        if (tree.right): 
            print(tree.right.value, end = " ") 
  
    # Recur for left and right subtrees  
    elif (level > 2): 
        self.print_level_cousins(tree.left, val, level - 1)  
        self.print_level_cousins(tree.right, val, level - 1) 
  

  def list_cousins(self, tree, val):
    level = self.get_level(tree, val, 1)
    self.print_level_cousins(tree, val, level)
    pass

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

Solution().list_cousins(root, 5)
# [4, 6]
