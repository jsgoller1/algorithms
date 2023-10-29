class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        edits = 0
        openers = 0
        for c in s:
            if c == '(':
                openers += 1
            else:  # ')'
                if openers == 0:
                    edits += 1
                else:
                    openers -= 1
        return edits + openers


s = Solution()
cases = [
    ("", 0),
    ("())", 1),
    ("(((", 3),
    (")))(((", 6),
]
for string, expected in cases:
    actual = s.minAddToMakeValid(string)
    assert actual == expected, f"{case}: {actual} != {expected}"
