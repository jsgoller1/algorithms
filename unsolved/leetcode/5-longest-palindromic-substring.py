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
Understand

In: String
Out: String, a substring of the input

This is similar to the longest palindromic subsequence problem, except that the characters
chosen must be contiguous, and we must actually store what string it is (although using start/end
indices, this can be done in O(c) space)

Thoughts / questions:
- We are likely going to look at the same characters many times; is there a way that we can definitively
rule out that a particular character isn't part of the longest substring?

Observations:
- We can check if a string is a palindrome by starting at the middle index and comparing characters;
a length-n string is a palindrome if the string[0] == string[n-1], string[1] == string[n-2], and so on.

- Every palindrome must have a valid sub-palindrome that is either 1 or 2 characters shorter;
if we're testing it starting and the middle then each time we test one or two characters, either
1) it is still a palindrome, or 2) it is not a palindrome and cannot be regardless of how
many characters are added:

Bottom-up testing:
....B..... -> palindrome by definition
...CBA.... -> not a palindrome regardless of how many characters we add
...BAB.... -> is a palindrome, may not be if we add more characters.

Top down testing:
ABA -> B (2 less)
ACATACA -> CATAC (2 less)
BBB -> BB (1 less)

Approaches:
  - Brute force: Longest = 0. For each character in the string[1:len(string)-1], test starting middle out. If the characters don't match,
    continue to the next testing. Otherwise, continue testing until we exhaust the string or it becomes a non-palindrome. Stop examining the
    string either at the len-2 character, or the Longest charcter, then double longest and return (see below for pseudocode).
  -

----
Plan

total = 1
halt = len(string)-1
str_start = 0
str_end = 0

for i in 1 to halt:
  if i >= halt - total/2:
    break

  curr, start, end = middle_out_test(i, string)
  if curr > total:
    str_start = start
    str_end = end
    total = curr

if total > 1:
  return string[start:end]
else:
  return string[0]

----
E
----
R
"""


def middle_out_test(i, string):
    start = i - 1
    start = i + 1

    return total, start, end


class Solution:
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: str
        """
        if len(string) == 1:
            return string

        if len(string) == 2:
            if string[0] == string[1]:
                return string
            else:
                return string[0]

        total = 1
        halt = len(string)-1
        str_start = 0
        str_end = 0

        for i in 1 to halt:
            if i >= halt - total/2:
                break

            curr, start, end = middle_out_test(i, string)
            if curr > total:
                str_start = start
                str_end = end
                total = curr

        if total > 1:
            return string[start:end]
        else:
            return string[0]


if __name__ == '__main__':
