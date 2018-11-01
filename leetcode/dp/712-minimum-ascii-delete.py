"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

in: two strings, s1 and s2
out: int, sum of ascii values to remove

Note:
- 0 < s1.length, s2.length <= 1000.
- All elements of each string will have an ASCII value in [97, 122].
------------------------------------------------------------------
This is a longest common subsequence problem
- Deleting characters from the string will create subsequences of it.
- By looking for the "lowest cost" one, we are inherently looking to remove
as few characters as possible, therefore a longer common subsequence is
preferred to a shorter one.
- Because there can be multiple LCSs, we want to pick the one that has the
highest value of the ascii characters, where the value is the sum
of ord(char) for each char.

Can we reuse the "how many characters must be deleted" DP method from #583?
  X e a t
X 0 1 2 3
s 1 2 3 4
e 2 1 2 3
a 3 2 1 2

s 115
e 101
a 97
t 116

if chars equal, take row-1, col-1
if not, take min of above and left, add opposite char to it and insert

   X    e    a    t    s1
X  0   101  198  314
s 115  216  313  329
e 216  115  212  328
a 313  212  115  231

s2

"""

import collections


class Solution:
    def minimumDeleteSum(self, s1, s2):
        costs = [[0 for col in range(len(s1) + 1)]
                 for row in range(len(s2) + 1)]
        for col, char in enumerate(s1, 1):
            costs[0][col] = ord(char) + costs[0][col-1]
        for row, char in enumerate(s2, 1):
            costs[row][0] = ord(char) + costs[row-1][0]

        for row, char2 in enumerate(s2, 1):
            for col, char1 in enumerate(s1, 1):
                if char1 == char2:
                    costs[row][col] = costs[row-1][col - 1]
                else:
                    costs[row][col] = min(
                        costs[row][col - 1] + ord(char1), costs[row-1][col] + ord(char2))
        return costs[-1][-1]


if __name__ == '__main__':
    s = Solution()
    assert s.minimumDeleteSum('sea', 'sea') == 0
    assert s.minimumDeleteSum('sea', 'eat') == 231
    assert s.minimumDeleteSum('delete', 'leet') == 403
    assert s.minimumDeleteSum("ccaccjp", "fwosarcwge") == 1399
    assert s.minimumDeleteSum("caabcccaccccca", "cacbaaac") == 1178
