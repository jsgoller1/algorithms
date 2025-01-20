"""
- O(n) time - check neighbors of each element, starting at idx 0, halt at first one
- Nums cannot be equal to neighors, always must go up or down
- if idxs 0 and -1 are equal, peak in middle.
- Another way to think of this is just a bin search for a maximal element (even if there are many)

O(log(n)) - adjusted binary search where we halve the array by keeping indices of max and moving inwards?
- when we get midpoint:
    - must pick m as new l or r. If m < l,r pick max(l,r) (or either if l=r). If m > l,r
"""


class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m] < arr[m+1]:
                l = m+1
            else:  # arr[m-1] > arr[m]:
                r = m-1
        return l


s = Solution()
for i, case in enumerate([
    ([1, 6, 5, 4, 3, 2, 1], set([1])),
    ([1, 2, 3, 4, 5, 6, 1], set([5])),
    ([10, 100, 0, 100, 10], set([1, 3])),
    ([4, 3, 2, 6], set([0, 3])),
    ([4, 3, 2, 4], set([0, 3])),
    ([4, 3, 2, 1], set([0])),
    ([1, 2, 3, 1], set([2])),
    ([1, 2, 1, 3, 5, 6, 4], set([1, 5])),
    ([1, 2, 1, 2, 1, 2], set([1, 3, 5]))
]):
    arr, valids = case
    peak = s.findPeakElement(arr)
    assert peak in valids, f"{i}, {arr}: {peak} not in {valids}"
