class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[-1] == len(arr):
            return len(arr) + k
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            missing = arr[m] - (m + 1)
            if missing >= k:
                r = m - 1
            else:
                l = m + 1
        missing = arr[l-1] - l
        remaining = k - missing
        return arr[l-1] + remaining
