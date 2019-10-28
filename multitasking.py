"""
We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
"""

def is_cooling_down(cooling_down, task):
  result = False
  for i in cooling_down:
    i[1] = i[1] - 1
    if i[0] == task:
      result = True
    if i[1] <= 0:
      cooling_down.remove(i)
  return result

def findTime(arr, cooldown):
  time = 0
  cooling_down = []
  how_it_happened = ''
  for i in arr:
    while is_cooling_down(cooling_down, i):
      how_it_happened = how_it_happened + '_ '
      time = time + 1
    cooling_down.append([i, cooldown])
    how_it_happened = how_it_happened + str(i) + ' '
    time = time + 1
  print(how_it_happened)
  return time 

print(findTime([1, 1, 2, 1], 3))
# 7