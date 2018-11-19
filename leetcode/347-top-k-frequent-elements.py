"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
--------------------------------------------------------------------
In: list[int], int
Out: list[int]

Constraints:
  - Must be better than n*log(n)
  - k will always be between 1 and count of unique elements

- Counting the elements is pretty easy; just keep a dict
mapping the int to count of occurences (O(n))
- One option could be to write a custom comparison
function for sort that would look up the key in the
occurences dict and sort based on that
- Then we could return a slice of the sorted keys
- Could we use Counters to efficiently solve this problem?
--------------------------------------
- get counts of all characters in dict
- sort using sorted with a custom key that looks up count
- return slice of "sorted" keys

pseudoKey(val1, val2):
  if val1 not in counts or val2 not in counts:
    throw an error
  else:
    return counts[val1] < counts[val2]

pseudo(arr, k):
  counts = {}
  for each char in arr:
    counts[char]++  // use default dict

  sort(arr, pseudoKey)

  return arr[:k]

- Cases:
  - k is never larger than size
  - empty array, return empty
    - will this break sorted()?
  - one element (return the one element)
  - no most frequent elements; what do we do as tiebreakers?
    - for now, any element that is kth most frequent may be returned
----------------------------------
- Python3 doesn't support cmp (didn't know, was in car with no internet)
- We can convert the counter to a list of tuples, sort that via the key arg,
and then construct a list to return based on that
"""

import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)
        sortable = [(key, counts[key]) for key in counts.keys()]
        sortable.sort(key=lambda tup: tup[1], reverse=True)
        return [sortable[tup][0] for tup in range(k)]


if __name__ == '__main__':
    s = Solution()
    assert s.topKFrequent([i for i in range(10)], 3) == [0, 1, 2]
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1, 1, 1], 1) == [1]
    assert s.topKFrequent([1], 1) == [1]
    assert s.topKFrequent([], 0) == []
