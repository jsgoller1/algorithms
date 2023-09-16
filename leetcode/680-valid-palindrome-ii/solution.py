class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(l: int, r: int, can_skip: bool):
            while 0 <= l < r < len(s):
                if s[l] != s[r]:
                    return (verify(l+1, r, False) or verify(l, r-1, False)) if can_skip else False
                l += 1
                r -= 1
            return True
        return verify(0, len(s)-1, True)


s = Solution()
cases = [
    ("a", True),
    ("aa", True),
    ("ac", True),
    ("abc", False),
    ("cabc", True),
    ("acbc", True),
]
for string, expected in cases:
    actual = s.validPalindrome(string)
    assert actual == expected, f"{string}: {actual} != {expected}"
