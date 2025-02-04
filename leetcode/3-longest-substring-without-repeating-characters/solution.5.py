"""
Two pointer approach with counter
"""

from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        longest = 1
        ctr = Counter({s[l]: 1})
        while r < len(s):
            ctr[s[r]] += 1
            while ctr[s[r]] > 1:
                ctr[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest
