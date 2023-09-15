from string import ascii_lowercase, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while 0 <= l < r < len(s):
            while (s[l].lower() not in ascii_lowercase) and (s[l].lower() not in digits):
                l += 1
            while (s[r].lower() not in ascii_lowercase) and (s[r].lower() not in digits):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = Solution()
assert s.isPalindrome("")
assert s.isPalindrome("a")
assert not s.isPalindrome("ab")
assert s.isPalindrome("aba")
assert s.isPalindrome("ab:a")
assert s.isPalindrome("A         b:a")
