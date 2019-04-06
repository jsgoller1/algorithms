"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
----
Understand

In: String
Out: String, a substring of the input

- There is a linear time solution to this problem called Manacher's Algorithm, but I haven't fully worked
out how it works yet.
- The brute force solution to this is:
  - go through each index in the string
  - at each given index, find the longest palindrome that has that index as the center
  - return the longest palindrome we can find.
- There's some ability to quit early from the brute force approach - for instance, from any given index,
the longest possible palindrome we can find will be min(distance from left edge, distance from right edge).
E.g. if the string is 10 characters long, no index after 5 can have a palindrome of length 10, so if our longest
is 10, quit there.
- We will start with the "test at every index" and optimize if we get TLE.
- Note that we need to return THE palindrome, not just the length; we should therefore
keep indices in the given string, and the length
---------------------------------------------------------
- initial palindrome test doesn't work
  - it correctly finds "bcb" in "abcba", but not "bb" in "abba".
  - cases:
    - 'abcba' -> bcb
      - We can catch this if we do our middle-out test, but not a 'two at a time'
    - 'abba' -> bb
"""


class Solution:
    def longestEvenPalindromeAtIndex(self, s, index):
        # test via "two at a time"
        left = index
        right = index + 1
        if right >= len(s) or s[left] != s[right]:
            return left, left

        while (0 < left and right < len(s)-1 and s[left - 1] == s[right + 1]):
            left -= 1
            right += 1
        return left, right

    def longestOddPalindromeAtIndex(self, s, index):
        # test via center index
        left = right = index
        while (0 < left and right < len(s)-1 and s[left - 1] == s[right + 1]):
            left -= 1
            right += 1
        return left, right

    def longestPalindrome(self, string):
        maxLeft = 0
        maxRight = 0
        for i, _ in enumerate(string):
            newLeft, newRight = self.longestEvenPalindromeAtIndex(string, i)
            if (maxRight - maxLeft) < (newRight - newLeft):
                maxLeft, maxRight = newLeft, newRight
            newLeft, newRight = self.longestOddPalindromeAtIndex(string, i)
            if (maxRight - maxLeft) < (newRight - newLeft):
                maxLeft, maxRight = newLeft, newRight
        return string[maxLeft:maxRight+1]


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome("babad") in ["bab", "aba"]
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("aaa") == "aaa"
    assert s.longestPalindrome("") == ""
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("aa") == "aa"
    assert s.longestPalindrome("ab") in ['a', 'b']
