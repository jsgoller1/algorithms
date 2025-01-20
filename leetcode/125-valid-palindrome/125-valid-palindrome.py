from string import ascii_letters, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valids = ascii_letters+digits
        l, r = 0, len(s)-1
        while l < r:
            if s[l] not in valids:
                l += 1
                continue
            if s[r] not in valids:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True


s = Solution()
for i, case in enumerate([
    ("0p", False),
    ("aba", True),
    ("a ba", True),
    ("a b:a", True),
    ("a:::::::", True),
    ("a", True),
    (" ", True),
    ("ca", False),
    ("cde", False)
]):
    string, expected = case
    actual = s.isPalindrome(string)
    assert actual == expected, f"{i}: {string}; {actual} != {expected}"
