"""
The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
Input: [3, 5, 0, 1, 3]
Output: 3
Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.
"""

def hIndex(publications):
  publications.sort()
  for index, citations in enumerate(publications):
    if citations > len(publications):
      break

    if citations <= len(publications)-index:
      h_index = citations

  return h_index

print(hIndex([5, 3, 3, 1, 0]))
# 3