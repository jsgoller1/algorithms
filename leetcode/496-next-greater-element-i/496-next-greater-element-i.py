"""
Brute force (quadratic): check right of every element 
Can O(1) determine if we need next greatest element of item in nums1 with dict (default -1)
Can't just keep track of max/min seen so far - next greatest for some nums2[i] might be in between
nlogn - can we sort nums2 array as pairs (val, idx in nums2)
    - finding the next element whose idx is greater is still possibly quadratic 
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for val in reversed(nums2):
            while stack and stack[-1] < val:
                stack.pop()
            next_greater[val] = stack[-1] if stack else -1
            stack.append(val)
        return [next_greater[num] for num in nums1]


s = Solution()
for nums1, nums2, expected in [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1])
]:
    actual = s.nextGreaterElement(nums1, nums2)
    assert actual == expected, f"{nums1}, {nums2}: {actual} != {expected}"
