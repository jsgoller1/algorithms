from itertools import *

"""
Statement: https://leetcode.com/problems/longest-palindromic-subsequence/description/

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: "cbbd"
Output: 2
One possible longest palindromic subsequence is "bb".

----
Understand


In - string
Out - int; the length of the longest subsequence of s
Constraints:
  - 0 <= len(s) <= 1000

General thoughts:
- A subsequence is s with 0 to len(s) characters removed.
- A palindrome is a sequence that reads the same backward as forward, e.g., madam or nurses run.

I found this under the problems tagged with "dynamic programming",
so I am biased towards solving it that way. However, notice that:
- We are given data in which we are trying to find a "key subcombination"
- The naive approach is O(n!)
- We are being asked to return a value describing that subcombination, not the subcombination itself.

These are three things that happen frequently in problems solvable with DP, and hint that we can
probably find a linear time, constant space solution since we probably don't need to maintain the specific
subcombination during execution.

The DP question: for an intermediary step n, what do we need to know about n-1 to determine the answer for n? We
should NOT need to know about every previous step. Some cases:
"b" -> 1
"ba" -> 1
"bab" -> 3
"baba" -> 3
"babab" -> 5
"cattac" -> 6
"rcjaqtftgaczl" -> 6 (same as above but with random unique letters tossed in)

- Can't remove unique chars in the string; they could show up in the middle
- what about working from the edges towards the middle?
  - Would be O(n^2)
  - Wouldn't be able to just stop at the middle, consider "azzzbcdefghijklmnopqrstuv".

Some possible approaches:
  - Brute force approach (this is still probably going to be
    bad even if we apply caching; in worst case, we check
    all possible subsequences, or the powerset of the sequence which is O(2^n)):
    - Exit if s is empty
    - For i in range(0, len(s)):
      - remove s[i] from the string
      - check if it's a palindrome
      - if yes, we found the longest one
      - if no, recurse with mutated s.

----
P
----
E
----
R
"""


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """


if __name__ == '__main__':
    print((powerset('abcde')))
    print(2**5)
    #s = Solution()
    #assert s.longestPalindromeSubseq("") == 0
    #assert s.longestPalindromeSubseq("a") == 1
    #assert s.longestPalindromeSubseq("bbbab") == 4
    #assert s.longestPalindromeSubseq("cbbd") == 2
