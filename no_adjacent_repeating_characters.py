"""
Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca
"""

class HeapNode():
  def __init__(self, char, freq):
    self.char = char 
    self.freq = freq

class PriorityQueue():
  def __init__(self):
    self.list = []

  def insert(self, node):
    self.list.append(node)

  def getMax(self):
    if len(self.list) <= 0:
      pass

    maxIndex = 0
    for i in range(len(self.list)):
      if self.list[i].freq > self.list[maxIndex].freq:
        maxIndex = i

    if self.list[maxIndex].freq > 0:
      self.list[maxIndex].freq = self.list[maxIndex].freq - 1
      return self.list[maxIndex].char
    else:
      pass


def rearrangeString(s):
  freq = [0] * 26
  for char in s:
    freq[ord(char) - ord('a')] = freq[ord(char) - ord('a')] + 1

  pq = PriorityQueue()
  for i in range(26):
    pq.insert(HeapNode(chr(ord('a') + i), freq[i]))

  result = ''
  lastMax = ''

  for i in range(len(s)):
    maxFreqChar = pq.getMax()
    result = result + maxFreqChar
    if lastMax == maxFreqChar:
      return
    lastMax = maxFreqChar

  return result

  

print(rearrangeString('abbccc'))
# cbcabc
