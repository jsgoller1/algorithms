"""
Need to make k many ribbons of equal length, and must be as long as possible.
How long can they be?

If k > sum(ribbons), 0. 
If k = sum(ribbons), 1. 
Otherwise, we have to make k-len(ribbons) many cuts at minimum.

Other thoughts: 
- Reversed sort first? Greatest length one seems most important / bounding factor for x. 
- Cutting longest in half gives us longest possible if we intend to reuse both halves. 
- If we don't cut ribbons equally (e.g. 7 and 2 from 9), we're basically just shortening 
existing ones. How do we know when to cut and use remainder versus cut and discard? 
- We can't just look at the minimum in the array and try to make that our x. 
Consider [100,10,10,10], k = 4 -> 25 (cut the 100 to 50s, then to 25s). Wrong to just pick 10 here. 
- How do we tell the [100,10,10,10] k=4 case (divide the longest repeatedly) from the [9,7,5] k=3 case
(trim all three down)? Same thing for [50,50,10,10], k=4

(worked with ChatGPT on this one)
"""

class Solution:
    def numberOfRibbons(self, ribbons, x):
        total = 0
        for ribbon in ribbons:
            total += ribbon // x
        return total 

    def maxLength(self, ribbons: List[int], k: int) -> int:
        totalLen = sum(ribbons)
        if totalLen < k:
            return 0
        if totalLen == k:
            return 1

        most = 0
        lo, hi = 1, max(ribbons)
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.numberOfRibbons(ribbons, mid) >= k:
                most = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return most
