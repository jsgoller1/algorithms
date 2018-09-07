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

To find in linear time a longest palindrome in a string, an algorithm may take advantage
of the following characteristics or observations about a palindrome and a sub-palindrome.
On the Wikipedia page, there are 8 observations about 3 different cases of palindromes -
here they are organized by cases. In the following, assume we know prior that P1, P2,
and P3 are known to be palindromes:

Observation #1
The left side of a palindrome is a mirror image of its right side.

Examples:
      L      R
P1: A B Z | Z B A
P2:     B | B
P3:     C A C

-----------------------------------
Case 1:

Observation #2
A third palindrome whose center is within the right side of a first palindrome will have
exactly the same length as that of a second palindrome anchored at the mirror center on the left side,
if the second palindrome is within the bounds of the first palindrome by at least one character (not
meeting the left bound of the first palindrome).

Example
P1:  C B A B Q Z Q B A B C
P2:    B A B
P3:                B A B

Explanation: P3's size equaling P2's and its center being at 8 are implied by P2's size center at 2
and the fact that they both lie cleanly within known palindrome P1. If either fell outside of P1,
we wouldn't be able to imply this. Below, P2 falls outside of P1, so it having a "mirror center" to P3
is not implied.

P1:       B A B Q B A B
P2:   B R B
P3:               B A B

-----------------------------------
Case 2:

Observation #3
If the second palindrome meets or extends beyond the left bound of the first palindrome,
then the distance from the center of the second palindrome to the left bound of the first palindrome
is exactly equal to the distance from the center of the third palindrome to the right bound of the
first palindrome.

P1:     B A B Q Z Q B A B
        |-|
P2: Z Q B A B Q Z
                      |-|
P3:             Z Q B A B Q Z

Explanation: In the above, P2's center A is one character away from the left boundary B of
P1, and this implies that P3's center A will be 1 character way from the right boundary B of P1.
Note that as stated, this is only true if the center of P2 and P3 both fall within P1. Observe how
the above case doesn't hold when P2 or P3's center falls outside of P1:

P1:           B A B Q B A B
P2:   B A Q A B
          |-2-|           |---3---|
P3:                     A B Z N O X O N Z B A

Observation #4
To find the length of the third palindrome under Case 2, the next character after the
right outermost character of the first palindrome would then be compared with its mirror
character about the center of the third palindrome, until there is no match or no more
characters to compare.

P1:     B A B Q Z Q B A B
P3:             Z Q B A B Q Z
                2 1   *   1 2
                2 1       1 2

Explanation: We do not know how long P3 is, but we know where its
center is, annotated by *. We then walk from the right outermost
character of P1, comparing with the equivalent character on the
opposite side of P3. Note again that this fails if the center
of P3 does not fall within P1 (as then we'd have no way of
inferring where the end of P3 is outside of P1):

P1:     B A B Q Z Q B A B
P3:                   A B Q Z R D R Z Q B A
                                *

-----------------------------------
(Case 3)

Observation #5
Neither the first nor second palindrome provides information
to help determine the palindromic length of a fourth palindrome
whose center is outside the right side of the first palindrome.

P1:     B A B Q Z Q B A B
P2:   Q B A B Q
P3:                 B A B
P4:                 B A B Z R D R Z B A B

Observation #6
It is therefore desirable to have a palindrome as a reference (i.e., the role of the first palindrome)
that possesses characters farthest to the right in a string when determining from left to right the palindromic
length of a substring in the string (and consequently, the third palindrome in Case 2 and the fourth palindrome
in Case 3 could replace the first palindrome to become the new reference).

-----------------------------------
Observation #7
Regarding the time complexity of palindromic length determination for each character
in a string: there is no character comparison for Case 1, while for Cases 2 and 3 only
the characters in the string beyond the right outermost character of the reference
palindrome are candidates for comparison (and consequently Case 3 always results in a
new reference palindrome while Case 2 does so only if the third palindrome is
actually longer than its guaranteed minimum length).

-----------------------------------
Observation #8
For even-length palindromes, the center is at the boundary of the two characters in the middle.

Examples:
      1 2 3 4 5 6 7 8
P1:   A B C D|D C B A
P2:   A B|B A
P3:   A|A

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
