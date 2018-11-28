"""
Find the kth largest element in an unsorted array. Note that it is the
 kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
------------------------------------------------------------
In: List[int]
Out: Int
- K will always be valid

Edge cases:
  - Empty list
  - Singleton list
  - List of all duplicates
  - List of all distinct

- Is there a reason we can't get the distinct elements,
sort them into a list, and then return the kth one?
- Kth largest element in sorted order; so can we just sort and return arr[k]?
- Why is this a medium question? What weird cases am I missing
--------------------------------------------------------------
pseudo(arr, k):
  sorted(arr)
  return arr[-k]
"""

class Solution:
    def findKthLargest(self, nums, k):
      if nums == []:
        return
      nums.sort()
      return nums[-k]

if __name__ == '__main__':
  s = Solution()
  assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
  assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
  assert s.findKthLargest([1,1,1,1,1,1,1], 3) == 1
  assert s,findKthLargest([], 0) == None
