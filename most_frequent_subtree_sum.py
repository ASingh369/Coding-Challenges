"""
Given a binary tree, find the most frequent subtree sum.

Example:

   3
  / \
 1   -3

The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

If there is a tie between the most frequent sum, you can return any one of them.

"""

class Node():
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def replace_with_sum(root):
  if root.left == None and root.right == None:
    pass
  else:
    replace_with_sum(root.left)
    replace_with_sum(root.right)
    if root.left == None and root.right != None:
      root.val = root.val + root.right.val 
    elif root.right == None and root.left != None:
      root.val = root.val + root.left.val 
    else:
      root.val = root.val + root.left.val + root.right.val


def most_repeating_node(root):
  count_arr = []
  stack = []
  while True:
    if root is not None:
      stack.append(root)
      root = root.left
    elif stack:
      root = stack.pop()
      already_exists = False
      for i in count_arr:
        if i[0] == root.val:
          already_exists = True
          i[1] = i[1] + 1
      
      if not already_exists:
        count_arr.append([root.val, 1])

      root = root.right
    else:
      break

  if count_arr:
    maximum = count_arr[0]
    for i in count_arr:
      if i[1] > maximum[1]:
        maximum = i
    return maximum[0]



def most_freq_subtree_sum(root):
  # replace all root nodes with sum
  replace_with_sum(root)

  # find most repeating node
  output = most_repeating_node(root)

  return output


root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
# 1