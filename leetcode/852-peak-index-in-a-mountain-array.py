"""
In: List of ints
Out: int, index of peak

- Input is definitely a mountain; i.e. for some index everything left and right is less
- can be up to 10,000 elements; should we try to terminate early?
  - no; the array isn't necesarily monotonic increasing/decreasing, there is just a peak
  - heights are positive
  where the property holds
- Is a plataeu a mountain, i.e. [0,1,1,0]?
- Can we just get the max of the array and return the index? O(n), O(c) space
--------
- linear search for max element, save index
"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        peak = 0
        peakIdx = 0
        for i, height in enumerate(A):
            if peak < height:
                peak = height
                peakIdx = i
        return peakIdx


if __name__ == '__main__':
    s = Solution()
    assert s.peakIndexInMountainArray([0, 1, 0]) == 1
    assert s.peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert s.peakIndexInMountainArray([6, 2, 1, 0]) == 0
    assert s.peakIndexInMountainArray([0, 1, 2, 3, 2, 6, 4, 3, 2]) == 5
