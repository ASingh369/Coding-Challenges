"""
A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and will be considered off the board.
"""

"""
Check if new location is inside the board
"""
def new_location(x, y):
  if x >= 0 and y >= 0 and x <= 8 and y < 8:
    return True
  return False

def is_knight_on_board(x, y, k, cache={}):
  if k == 0:
    return 1

  result = 0

  # Move to top right
  if new_location(x+1, y+2):
    result = result + 0.125 * is_knight_on_board(x+1, y+2, k-1)
  
  # Move to top left
  if new_location(x-1, y+2):
    result = result + 0.125 * is_knight_on_board(x-1, y+2, k-1)
  
  # Move to right top
  if new_location(x+2, y+1):
    result = result + 0.125 * is_knight_on_board(x+2, y+1, k-1)
  
  # Move to right bottom
  if new_location(x+2, y-1):
    result = result + 0.125 * is_knight_on_board(x+2, y-1, k-1)
  
  # Move to bottom left
  if new_location(x-1, y-2):
    result = result + 0.125 * is_knight_on_board(x-1, y-2, k-1)
  
  # Move to bottom right
  if new_location(x+1, y-2):
    result = result + 0.125 * is_knight_on_board(x+1, y-2, k-1)
  
  # Move to left top
  if new_location(x-2, y+1):
    result = result + 0.125 * is_knight_on_board(x-2, y+1, k-1)
  
  # Move to left bottom
  if new_location(x-2, y-1):
    result = result + 0.125 * is_knight_on_board(x-2, y-1, k-1)

  return result


print(is_knight_on_board(0, 0, 1))
# 0.25
print(is_knight_on_board(0, 0, 3))
# 0.125