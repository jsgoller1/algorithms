"""
Implement atoi which converts a string to an integer. The function
first discards as many whitespace characters as necessary until the
first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed
by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form
the integral number, which are ignored and have no effect on the
behavior of this function.

If the first sequence of non-whitespace characters in str is
not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters,
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
- Only the space character ' ' is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
---------------------------------------------------------------------------------
- lots of downvotes for this question
- detect if invalid (empty, leading characters)
- parse out valid characters; detect leading -
- convert to numeric representation
  - iterative multiplication by 10
- apply negative, and return

"""


class Solution:
    def myAtoi(self, string):
        result = 0
        negative = False
        digits = []

        # Remove leading whitespace
        characters = []
        i = 0
        while i < len(string) and string[i].isspace():
            i += 1

        # Detect leading - or +
        if i < len(string) and string[i] in ['-', '+']:
            negative = string[i] == '-'
            i += 1

        # Get valid digits
        while i < len(string) and string[i].isdigit():
            digits.append(string[i])
            i += 1

        # Convert to int
        place = 1
        while digits:
            result += int(digits.pop()) * place
            place *= 10

        # Prevent "overflow"
        result *= [1, -1][negative]
        result = max(-(2 ** 31), result)
        result = min(result, (2**31) - 1)

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('+0 123') == 0
    assert s.myAtoi("") == 0
    assert s.myAtoi("+1") == 1
    assert s.myAtoi("42") == 42
    assert s.myAtoi("   -42") == -42
    assert s.myAtoi("4193 with words") == 4193  # lol what even
    assert s.myAtoi("words and 987") == 0
    assert s.myAtoi("-91283472332") == -2147483648
