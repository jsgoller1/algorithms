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
to work our way up.

If we are looking at the k-th element in a string
of n characters, we only need to know how many possible ways we can decode
the k-1th and k-2th characters; adding these is the number of ways to decode
the kth character. If there's zero ways to decode the kth character, we return
zero immediately. Our initialization (instead of base-cases) is for the last
and second-to-last elements.

pseudocode:
k-2 = 1 if decode(second to last) and decode(last), else 0
k-1 = 1 if decode(last two) + k-2
for each char from third to last to first:
    if k-1 + k-2 == 0:
        return 0
    if not zero:
        k = k-1 + k-2 if decode(current + current-1), else k = k-1
        k-2 = k-1
        k-1 = k
    if zero:
        k-2 = k-1
        k-1 = 0
        k = 0

Some examples:
1120 (decode as 1,1,20 and 11,20)
   0
  1
 1
2

If we hit a zero mid string, it means that one-decodings are not possible at that point,
so we should only carry forward two-decodings.
1020 (decode only as 10,20)
   0
  1
 0 <--- set k-2 to k-1, k-1 to zero, then go to next iteration.
1 <- k-1 + k-2

However, we should fail if we see two zeros:
10020 (invalid)
    0
   1
  0 <- k-2 set to k-1 (1), k-1 set to zero
 0 <- fail, k-2 + k-1 = 0

Some examples for if we see a 2-decoding that is invalid, such as 40:
1040 (invalid)
   0
  0
 x <- fails here, exits on first loop

10411 (only valid decodings are 10,4,1,1 and 10,4,11)
    1
   2
  2 <- only look at k-1, as the 41 would render all k-2 decodings invalid.
 0 <- k-1 is invalid for zero
2
----
Execute

See below.
----
Review

"""

cache = {}


def valid_decode(string):
    if 0 < len(string) < 3 and 1 <= int(string) <= 26 and string[0] != '0':
        return 1
    else:
        return 0


class Solution:
    def numDecodings_bu(self, string):
        """
        Iterative, constant-space solution (bottom up).
        """

        # Initialize
        k_2 = 0
        k_1 = 0
        k = 0
        if len(string):
            k_2 += valid_decode(string[-1])
            k = k_2
        if len(string) - 1:
            if valid_decode(string[-1]) and valid_decode(string[-2]):
                k_1 = k_2
            if valid_decode(string[-2:]):
                k_1 += 1
            k = k_1

        # Loop through remainder of string
        for i in range(len(string) - 3, -1, -1):
            if k_1 + k_2 == 0:
                return 0

            if string[i] != '0':
                if (valid_decode(string[i:i + 2])):
                    k = k_1 + k_2
                else:
                    k = k_1
                k_2 = k_1
                k_1 = k
            else:
                k_2 = k_1
                k_1 = 0
                k = 0

        return k

    def numDecodings(self, string):
        """
        Iterative, constant-time solution (top-down).

        Adapted from: https://leetcode.com/problems/decode-ways/discuss/30384/A-concise-dp-solution
        """
        # If the string is empty or begins with a '0', it has no valid decoding.
        if not string or string[0] == '0':
            return 0

        k_1 = 1
        k_2 = 1
        for i in range(1, len(string)):
            # If we encounter a zero, there are no valid one-character decodings at this position.
            if string[i] == '0':
                k_1 = 0

            # If we can decode a value between 10 and 26, there's also a valid two character decoding. So,
            # the current character has k_1 + k_2 decodings, and the old k_1 becomes k_2
            if string[i - 1] == '1' or string[i-1] == '2' and 0 <= int(string[i]) <= 6:
                k_1 = k_2 + k_1
                k_2 = k_1 - k_2

            # There's no valid two character decoding (i.e. '40'), so the old k_1 becomes k_2.
            else:
                k_2 = k_1

        return k_1


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings('0') == 0
    assert s.numDecodings('9') == 1
    assert s.numDecodings('40') == 0
    assert s.numDecodings('10') == 1
    assert s.numDecodings('11') == 2
    assert s.numDecodings('012') == 0
    assert s.numDecodings('440') == 0
    assert s.numDecodings('110') == 1
    assert s.numDecodings('229') == 2
    assert s.numDecodings('111') == 3
