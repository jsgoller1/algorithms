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

Some case analysis:
d(5) -> base case (1 string)
d(25) -> d(2) + d(5) && 25 (2 strings)
d(22) -> d(2) + d(2) && 22 (2 strings)
d(225) -> d(2) + d(25) && d(22) + d(5) (4 strings)
d(1225) -> d(1),d(225) && d(12), d(25)
----
Initial Plan

Having already solved this using a top-down approach in O(n) space, I am
going to attempt to solve it bottom-up with constant space.

Bottom up:
Instead of starting with the first and first two elements of the string
and trying to determine how many possible ways we can "break it down", we
could start from the last and last two elements of the string and try
to work our way up. We might be able to think of this as
----
Execute

See below.
----
Review

"""

cache = {}


def decode(string):
    if 0 < len(string) < 3 and 1 <= int(string) <= 26 and string[0] != '0':
        return chr(64 + int(string))


class Solution:
    def numDecodings(self, string):
        if string in cache:
            return cache[string]

        count = 0

        if len(string) <= 1:
            if decode(string):
                count += 1
            return count

        if len(string) == 2:
            if decode(string):
                count += 1
            if decode(string[0]) and decode(string[1]):
                count += 1
            return count

        if decode(string[:1]):
            count += self.numDecodings(string[1:])

        if decode(string[:2]):
            count += self.numDecodings(string[2:])

        cache[string] = count
        return count
