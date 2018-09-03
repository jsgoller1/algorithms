import collections
import random

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

We should have a helper function decode() that converts a number to a string, assuming it's between 1 and 26.
For our solve():
  base case: empty string - return []
Recursive case:
  return a list containing:
    - the first letter decoded + solve
  [decode([:1]) + string for every string in solve[1:] if valid decode] + [decode([0:2]) + string for every string in solve[2:] if valid decode]

d(5) -> base case (1 string)
d(25) -> d(2) + d(5) && 25 (2 strings)
d(22) -> d(2) + d(2) && 22 (2 strings)
d(225) -> d(2) + d(25) && d(22) + d(5) (4 strings)
d(1225) -> d(1),d(225) && d(12), d(25)
----
Execute
----
Review
"""

cache = {}


def decode(string):
    if 0 < len(string) < 3 and 1 <= int(string) <= 26 and string[0] != '0':
        return chr(64 + int(string))


def solve(string):
    if string in cache:
        return cache[string]

    if len(string) <= 1:
        if decode(string):
            return collections.deque([decode(string)])
        else:
            return collections.deque()

    if len(string) == 2:
        strings = collections.deque()
        if decode(string):
            strings.append(decode(string))
        if decode(string[0]) and decode(string[1]):
            strings.append(decode(string[0]) + decode(string[1]))
        return strings

    strings = collections.deque()
    if decode(string[:1]):
        for each in solve(string[1:]):
            strings.append(decode(string[:1]) + each)

    if decode(string[:2]):
        for each in solve(string[2:]):
            strings.append(decode(string[:2]) + each)

    cache[string] = strings
    return strings


class Solution:
    def numDecodings(self, s):
        solution = solve(s)
        # print(s)
        # print(solution)
        # print(len(solution))
        # print('-------')
        return len(solution)


if __name__ == '__main__':
    s = Solution()
    s.numDecodings('')
    s.numDecodings('0')
    s.numDecodings('4')
    s.numDecodings('01')
    s.numDecodings('12')
    s.numDecodings('10')
    s.numDecodings('62')
    s.numDecodings('1223134')
    s.numDecodings(
        "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
