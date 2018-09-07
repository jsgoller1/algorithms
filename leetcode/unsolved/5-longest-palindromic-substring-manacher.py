"""
Statement (of the problem): https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
----
Plan / Understand

While working on my own implementation of this, I discovered that the only
known linear-time solution to this problem was Manacher's algorithm.:
https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm

Here's a good explanation of Manacher's algorithm:
https://www.hackerrank.com/topics/manachers-algorithm

In the article:
- S is our input string of length N,
- P[] is an array containing the lengths of the "palindromic radius"
  of the palindromes centered at each index of T; P[4] = 5 means
  that the a palindrome in T centered at 4 is 10 long, with radius 5.
- T is the string formed after # is inserted.
- C is the center of the "reference palindrome" currently
  known to include the boundary closest to the right end of T.
- R is the rightmost boundary of the palindrome centered at C.
- i is the position of an element in T whose palindromic span
  is under consideration; i is always to the right of C.

So for the string "abba":

    0 1 2 3 4 5 6 7 8
    i'i'i'i'  i i i i

            C       R
T = # a # b # b # a #
P = 0 1 0 1 4 1 0 1 0

Note that i' = C - (i - C) = 2C-i.
Ex.
2  = 4 - (i - 4) = 2*4-i
2 = 8 - i
i + 2 = 8
i = 6

Example: Suppose S = "babcbabcbaccba".
Then T = "#b#a#b#c#b#a#b#c#b#a#c#c#b#a#".

As we examine T, we have three possible cases:

Case 1: Suppose we know about two palindromes P1,P2
in our string with P1 centered at C and P2 centered at
i'. Call the left boundary of P1 L. In case 1, the left
boundary of P2 falls to the right of L:

     L    C    R
T: #b#a#b#c#b#a#b#c#b#a#c#c#b#a#
P1:  #a#b#c#b#a#
P2     #b#
        i'

We know that T[C+k] = T[C-k] for all k < R - C (all characters
reflected across C are equal as long as they are between the
rightmost boundary and the center.)

----
Execute

See below
----
R
"""


class Solution:
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: str
        """
        pass


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome('babad') in ['aba', 'bab']
    assert s.longestPalindrome('aba') == 'aba'
    assert s.longestPalindrome('cbbd') == 'bb'
