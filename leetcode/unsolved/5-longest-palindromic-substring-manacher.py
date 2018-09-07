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
known linear-time solution to this problem was Manacher's algorithm:
https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
I will implement that algorithm here. and work through the notes for my own understanding.

Observations:
1. The left side of a palindrome is a mirror image of its right side.

Examples:
AA = [A  A]
ABBA = [AB  BA]
ABBCBBA = [ABB C BBA]

2. (Case 1) A third palindrome whose center is within the right side of a first palindrome will have
   exactly the same length as that of a second palindrome anchored at the mirror center on the left side,
   if the second palindrome is within the bounds of the first palindrome by at least one character (not
   meeting the left bound of the first palindrome).

Example
i     0 1 2 3 4 5 6 7 8 9 10
P1: [ C B A B Q Z Q B A B C ]
P2: [   B A B               ]
P3: [               B A B   ]

Explanation: P3's size equaling P2's and its center being at 8 are implied by:
- P2's size center at 2
- the fact that they both lie within known palindrome P1.

If either of these conditions were false, the implication wouldn't hold:
i     0 1 2 3 4 5 6 7 8
P1:     [ B A B Q B A B ]
P2: [ ? ? B             ]
P3: [             B A B ]
(P2 falls outside P1)

i     0 1 2 3 4 5 6
P1: [ Z A B Q B A B ]
P2: [ Z A B         ]
P3: [         B A B ]
(P1 isn't a palindrome1)


3. (Case 2) If the second palindrome meets or extends beyond the left bound of the first palindrome, then the distance from the center of the second palindrome to the left bound of the first palindrome is exactly equal to the distance from the center of the third palindrome to the right bound of the first palindrome.
4. To find the length of the third palindrome under Case 2, the next character after the right outermost character of the first palindrome would then be compared with its mirror character about the center of the third palindrome, until there is no match or no more characters to compare.
5. (Case 3) Neither the first nor second palindrome provides information to help determine the palindromic length of a fourth palindrome whose center is outside the right side of the first palindrome.
6. It is therefore desirable to have a palindrome as a reference (i.e., the role of the first palindrome) that possesses characters farthest to the right in a string when determining from left to right the palindromic length of a substring in the string (and consequently, the third palindrome in Case 2 and the fourth palindrome in Case 3 could replace the first palindrome to become the new reference).
7. Regarding the time complexity of palindromic length determination for each character in a string: there is no character comparison for Case 1, while for Cases 2 and 3 only the characters in the string beyond the right outermost character of the reference palindrome are candidates for comparison (and consequently Case 3 always results in a new reference palindrome while Case 2 does so only if the third palindrome is actually longer than its guaranteed minimum length).
8. For even-length palindromes, the center is at the boundary of the two characters in the middle.




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
