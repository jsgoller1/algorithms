"""
init count. Each time we see (, count++; each time ), count--
two passes:
    - first pass, remove any ) when our count would go negative
    - second pass, remove any ( when our count would be positive. 
    - return result 
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        first_pass = []
        for c in s:
            if c == "(":
                count += 1
                first_pass.append(c)
            elif c == ")":
                if count > 0:
                    count -= 1
                    first_pass.append(c)
            else:  # c is lower case char
                first_pass.append(c)
        if not count:
            return "".join(first_pass)
        second_pass = []
        for c in first_pass[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                second_pass.append(c)
        return "".join(second_pass[::-1])


s = Solution()
cases = [
    ("())()(((", "()()"),
    ("(((())()", "((()))"),
    ("", ""),
    ("a)b(c)d", "ab(c)d"),
    ("(a)b(c)d", "(a)b(c)d"),
    ("((a))(b(c)d)", "((a))(b(c)d)"),
    ("(((a))(b(c)d)", "((a))(b(c)d)"),
]
for string, expected in cases:
    actual = s.minRemoveToMakeValid(string)
    assert actual == expected, f"{string}: {actual} != {expected}"
