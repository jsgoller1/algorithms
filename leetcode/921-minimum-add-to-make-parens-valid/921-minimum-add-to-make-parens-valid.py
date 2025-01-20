class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_closers = 0
        balance = 0
        for c in s:
            if c == "(":
                balance += 1
            elif c == ")" and balance > 0:
                balance -= 1
            else:
                unmatched_closers += 1
        return balance + unmatched_closers


s = Solution()
for case, expected in [
    ("", 0),
    ("())", 1),
    ("(((", 3),
    (")))(((", 6)
]:
    actual = s.minAddToMakeValid(case)
    assert actual == expected, f"{case}: {actual} != {expected}"
