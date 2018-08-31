"""
Statement - https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

----
Understand

The input for this problem is a string containing integers; the output is an integer,
representing the possible number of strings we could produce.

This feels very much like a dynamic programming problem - once we know all of the
ways to decode an N-character number string, all we need to look at when adding
the n+1 character is the N string, and the n-1 string if the n+1 character is 1 or 2.

There might be an edge case around 0 - 20 is valid as twenty, but not as two-zero.
----
Plan

Keep a top level list
We should have a helper function decode() that converts a number to a string, assuming it's between 1 and 26.
For our solve():
  base case: one letter - return a [decode(letter)]
Recursive case:
  return [decode([:1]) + string for every string in solve[1:] if valid decode] + [decode([0:2]) + string for every string in solve[2:] if valid decode]

12345:
1 + solve(2345),
2 + solve(345), 23 + solve(45)

12 + solve(345)
3 + solve(45), 34 + solve(5)
----
Execute
----
Review
"""


def decode(numstr):
    num = int(numstr)
    if not (1 <= num <= 26):
        return ''
    return chr(65+num)


def solve(string):
    if not string:
        return ['']

    if len(string) == 1:
        return [decode(string)]

    single = []
    single_decoded = decode(string[:1])
    if single_decoded:
        single = [single_decoded + each for each in solve(string[1:])]

    double = []
    double_decoded = decode(string[:2])
    if double_decoded:
        double = [double_decoded + each for each in solve(string[2:])]

    return single + double


class Solution:
    def numDecodings(self, s):
        return len(solve(s))


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('0'))
    print(solve('0'))
