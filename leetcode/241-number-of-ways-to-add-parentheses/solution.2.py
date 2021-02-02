from typing import List


def compute(string, lo, hi):
    possible_ways = []
    for i in range(lo, hi+1):
        if string[i] in "-+*":
            lefts = compute(string, lo, i-1)
            rights = compute(string, i+1, hi)
            for left in lefts:
                for right in rights:
                    possible_ways.append(f"({left}{string[i]}{right})")
    return possible_ways if possible_ways else [f"({string[lo:hi+1]})"]


class Solution:
    def diffWaysToCompute(self, string: str) -> List[int]:
        return [eval(way) for way in compute(string, 0, len(string)-1)]


s = Solution()
cases = [
    ("2-1-1", [0, 2]),
    ("2*3-4*5", [-34, -14, -10, -10, 10]),
    ("11", [11]),
    ("10+5", [15])
]
for string, expected in cases:
    actual = s.diffWaysToCompute(string)
    assert sorted(actual) == sorted(expected), f"{string}: {expected} != {actual}"
