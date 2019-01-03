"""
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
-----------------------------------------
- In: two list[ints]
- Out: List[ints]

- This question has a ton of downvotes.

The easiest thing to do here is just append the two arrays and call sorted()
on them. The merging has to be in place, which means we can't use a mergesort-like
merge step with a third array that can be done in O(n) time. My intuition says that for
the in-place version, we might devolve into worse than O(n) time because of shifting
costs if using a contiguous array. In any event, an O(n) solution will be more complicated
and nlogn is a completely acceptable complexity.

Actually, simple appending didn't work because of the zeroes. Instead, we should
copy into the end of the first array and overwrite the values.
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = -1
        while nums2:
            nums1[i] = nums2.pop()
            i -= 1
        nums1.sort()


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 0, 0, 0]
    y = [2, 5, 6]
    s.merge(x, len(x), y, len(y))
    assert x == [1, 2, 2, 3, 5, 6]
