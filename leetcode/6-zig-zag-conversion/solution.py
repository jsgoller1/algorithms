"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

Constraints:
    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

Possible cases:
    - single letter string (given)
    - "Biggest": 1000 letters and 1000 rows
        - if len(str) <= rows, then the output is the same as the input; can easily test for this and save lots of work
    - Many letters, few rows
        - will require most work, except if 1 row (also fits into above case). 10000 letters and 2 rows will completely shuffle the string.
    - can also get a mix of case and comma/period but I don't think this changes anything
----------------------------------------
Is there a "brute force approach"?
    - Maybe trying all possible orderings of the string? Not sure why we'd want to do that

This feels more like a "tricky to implement" situation than "how can we do less work than brute force?"

One approach:
    Create: rows = {row_i: '' for row_i in range(rows)}
    Create a helper function / generator to determine which row the next letter should go in
    # will give 0 for the first, then 1 for second, and so on; breaks if there's 1 row (though we can catch this up front?)
    prev_row_1, prev_row_2 = 1, 2
    for i, letter in enum(string):
        row_i = get_next_row(i, prev_row)
        Append the letter to rows[row_i]
        prev_row_2, prev_row_1 = prev_row_1, row_i
    Return ''.join(rows.values)

Helper function:
    - Should capture the idea of "bouncing" off the ends of the rows
    - takes indexes of two previously used rows
    - if 0 < prev_1 < rows-1:
        return prev_1 + 1 if prev_1 > prev_2, else prev_ -1
    - else:
        return prev_1 - 1 if prev_1 > prev_2 else prev_1 + 1
"""
from collections import defaultdict
from typing import List


def get_next_row(rows, prev_1, prev_2):
    if 0 < prev_1 < rows-1:
        return prev_1 + 1 if prev_1 > prev_2 else prev_1 - 1
    else:
        return prev_1 - 1 if prev_1 > prev_2 else prev_1 + 1


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or len(s) <= num_rows:
            return s
        rows = defaultdict(str)

        prev_1, prev_2 = 1, 2
        for letter in s:
            next_row = get_next_row(num_rows, prev_1, prev_2)
            rows[next_row] += letter
            prev_2, prev_1 = prev_1, next_row

        return ''.join(rows.values())


if __name__ == '__main__':
    cases = [
        (4, 1, 2, 0),
        (4, 0, 1, 1),
        (4, 2, 1, 3),
        (4, 3, 2, 2),
    ]
    for rows, prev_1, prev_2, expected in cases:
        actual = get_next_row(rows, prev_1, prev_2)
        assert actual == expected, f"{rows}, {prev_1}, {prev_2}; {expected} != {actual}"

    sol = Solution()
    cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("PAYPALISHIRING", len("PAYPALISHIRING"), "PAYPALISHIRING"),
        ("PAYPALISHIRING", 1000, "PAYPALISHIRING"),
        ("A", 1, "A")
    ]
    for in_str, rows, expected in cases:
        actual = sol.convert(in_str, rows)
        assert expected == actual, f"{in_str, rows}, {expected} != {actual}"
