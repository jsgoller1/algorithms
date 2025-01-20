"""
- Can use `sorted()` but with a custom key function that relies on 
the order string
- Can also implement mergesort 
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ctr = Counter(s)
        sol = []
        for c in order:
            sol.append(c*ctr[c])
            del ctr[c]
        for c in ctr:
            sol.append(c*ctr[c])
        return ''.join(sol)


class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        order = {val: i for i, val in enumerate(order)}

        def custom(c):
            return order[c] if c in order else float('inf')
        return ''.join(sorted(list(s), key=custom))


sol = Solution()
for order, s, expected in [
    ('a', 'a', 'a'),
    ('a', 'q', 'q'),
    ('dcba', 'abcd',  'dcba'),
    ('dcba', 'abcdqqqq', 'dcbaqqqq')
]:
    actual = sol.customSortString(order, s)
    assert actual == expected, f"{order}, {s}: {actual} != {expected}"
