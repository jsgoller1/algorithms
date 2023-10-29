from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sorted_s = []
        chars = Counter(s)
        for c in order:
            if c in chars:
                sorted_s.append(c * chars[c])
                del chars[c]
        for k, v in chars.items():
            sorted_s.append(k * v)
        return ''.join(sorted_s)
