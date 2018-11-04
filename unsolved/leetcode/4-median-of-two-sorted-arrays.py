"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
---------------------------------------------
- The arrays overlap or they don't:
  - Overlapping [1,3,5],[2,4,6]
  - Not: [1,2,3],[4,5,6]

- Suppose we kept pointers into each array:
  - The former is simple - given length = len(arr1)+len(arr2), the median has length/2 chars
  to its left and to its right if odd, or
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return 0

if __name__ == '__main__':
  s = Solution([1, 3],[2]) == 2.0
  s.findMedianSortedArrays([1, 2],[3, 4]) == 2.5
