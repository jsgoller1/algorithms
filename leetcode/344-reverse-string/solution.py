"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"
-----------------------------------------
Input: string
output: string

- python doesn't support assigning to strings, so we have to convert to a list
- be mindful of off-by-ones
- go from start to mid swapping
"""


class Solution(object):
    def reverseString(self, s):
        chars = list(s)
        last = len(s)-1
        for i in range(len(s) // 2):
            chars[i], chars[last - i] = chars[last - i], chars[i]
        return ''.join(chars)


if __name__ == '__main__':
    s = Solution()
    testCases = ["dog", "ggg", "", "a", "gog"]
    for case in testCases:
        assert s.reverseString(case) == case[::-1]
