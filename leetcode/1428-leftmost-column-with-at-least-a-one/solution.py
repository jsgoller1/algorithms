# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        best = float('inf')
        m, n = binaryMatrix.dimensions()

        def binary_search(row_idx):
            best_so_far = float('inf')
            lo, hi = 0, n-1
            while lo <= hi:
                mid_idx = (hi + lo) // 2
                mid = binaryMatrix.get(row_idx, mid_idx)
                if mid == 1:
                    best_so_far = mid_idx
                    hi = mid_idx - 1
                else:
                    lo = mid_idx + 1
            return best_so_far

        for y in range(m):
            if binaryMatrix.get(y, m-1) == 1:
                best = min(best, binary_search(y))
        return best if best != float('inf') else -1
