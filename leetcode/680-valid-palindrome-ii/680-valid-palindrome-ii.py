class Solution:
    def validPalindromeNormal(self, substr: str) -> bool:
        l, r = 0, len(substr)-1
        used_deletion = False
        while l < r:
            if substr[l] != substr[r]:
                return False
            l, r = l+1, r-1
        return True

    def validPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.validPalindromeNormal(s[l+1:r+1]) or self.validPalindromeNormal(s[l:r])
            l, r = l+1, r-1
        return True


sol = Solution()
for string, expected in [
    ("abc", False),
    ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True),
    ("aba", True),
    ("aa", True),
    ("aabbc", False),
    ("aababa", True),
    ("acababa", False),
    ("abcabc", False)

]:
    actual = sol.validPalindrome(string)
    assert actual == expected, f"{string}: {actual} != {expected}"
