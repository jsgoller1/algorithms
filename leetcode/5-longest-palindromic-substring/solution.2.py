"""
Cubic time: test every substring (TLE)
Quadratic time: test every pair of ends (viable given constraints)
Linear time: Manacher's algorithm? Don't know it 

For Quadratic time approach, will also require quadratic space so 
we don't recompute 
"""

from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0, 0)
        q = deque()
        for i, _ in enumerate(s):
            q.append((i, i))
            if i + 1 < len(s) and s[i] == s[i + 1]:
                longest = (i, i + 1)
                q.append((i, i + 1))
        while q:
            l, r = q.popleft()
            longest = longest if longest[1] - longest[0] + 1 >= r - l + 1 else (l, r)
            nl, nr = l - 1, r + 1
            if 0 <= nl <= nr < len(s) and s[nl] == s[nr]:
                q.append((nl, nr))
        return s[longest[0] : longest[1] + 1]
