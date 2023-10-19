class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if not ribbons or sum(ribbons) < k:
            return 0

        ribbons.sort()
        lo, hi = 1, ribbons[-1]
        best = 1
        while lo <= hi:
            mid = (hi + lo)//2
            possible = sum(ribbon // mid for ribbon in ribbons)
            if possible >= k:
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
