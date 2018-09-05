import collections

"""
https://leetcode.com/problems/restore-ip-addresses/description/


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
---
Understand

In this problem, we will be taking a string of integers and
returning all valid possible IP addresses. A valid IP (v4)
address is of the form "x.x.x.x", where x is a number
between 0 and 255. There are no negative numbers, and no
strings greater than 255.

In: String
Out: List of strings
---
Plan

This problem calls for backtracking. At a high level, we
will look at different subdivisions of the string and
determine if we are able to be made into a valid IP. If not,
we will back out.

Some input cases to consider:
- If an input string is longer than 12 characters or shorter than
4 characters, it cannot be made into a valid IP address:
345 -> 3.4.5.? (too few values at minimum spacing between .)
1231231231234 -> 123.123.123.1234 (too many values at maximum spacing between .)

- If an input string is exactly 12 characters, it must contain at least 4 total
instances of 1 or 2 (we won't need to explicitly consider this, but it is interesting):
345.678.903.456 -> Not valid

Other considerations:
- We need to make sure there's at least 1 character between each '.'; 1..2.34 is invalid.


Pseudocode:
- check base case:
    - no remaining '.' to use
    - no remaining values to use
    - each value in between '.' is between 0 and 255 and no '.' is adjacent
        - If all true, add string to a global list of valid IPs and return true.
        - If not, back out.

# Otherwise, try (via string splicing so we don't get IndexErrors):
    # current string plus a '.', followed by undoing
    # current string plus one value, followed by undoing
    # current string plus two values, followed by undoing
    # current string plus three values, followed by undoing
---
Execute

See below.
---
Review

Time to solve: 1h45m.

My initially approach was generally right, but I goofed up on two major details:
- Should we represent the remaining things to add to the IP as strings or lists? I initially went with
strings because I though string splicing would make it easier, but it turned out that using lists/deques was shorter
and more intuitive. String splicing led to some weird edge cases.
- At each step, what is the next recursive step? Initially I tried adding a '.', one value, two values, and three values
to the end of the possible IP. However, we only really need to try either adding a dot or a value - the value case
will eventually try all cases that one/two/three values would try.
"""


def is_valid_ip(possible_ip):
    vals = [val for val in ''.join(possible_ip).split('.') if val != '']

    # Removing all '.' leaves 4 values in valid IPs
    if len(vals) != 4:
        return False

    for each in vals:
        # Correct ranges of values
        if not (0 <= int(each) <= 255):
            return False

        # 0 is a valid value, but a 01 and 010 aren't.
        if len(each) > 1 and each[0] == '0':
            return False

    return True


class Solution:
    def restoreIpAddresses(self, s):
        self.dots = ['.'] * 3
        self.values = collections.deque(list(s))
        self.valid_ips = []

        # Catch impossible cases
        if not (4 <= len(self.values) <= 12):
            return []

        self.solve([])
        return self.valid_ips

    def solve(self, possible_ip):
        # Check base case
        if not self.values:
            if not self.dots and is_valid_ip(possible_ip):
                return True
            else:  # Shouldn't have remaining dots and no values or invalid ips
                return False

        # Otherwise, recurse with backtracking
        # current possible IP plus a '.', followed by undoing
        if self.dots:
            possible_ip.append(self.dots.pop())
            # We don't need to check this, because an ip ending in '.' is never valid.
            self.solve(possible_ip)
            self.dots.append(possible_ip.pop())

        # current IP plus another value
        possible_ip.append(self.values.popleft())
        if self.solve(possible_ip):
            self.valid_ips.append(''.join(possible_ip))
        self.values.appendleft(possible_ip.pop())


if __name__ == '__main__':
    s = Solution()
    assert s.restoreIpAddresses("25525511135") == [
        "255.255.11.135", "255.255.111.35"]
