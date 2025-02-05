from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []

        def recurse(opens, closed, parens_list):
            if closed == n:
                solutions.append("".join(parens_list))
                return
            if opens < n:
                parens_list.append("(")
                recurse(opens + 1, closed, parens_list)
                parens_list.pop()
            if closed < opens:
                parens_list.append(")")
                recurse(opens, closed + 1, parens_list)
                parens_list.pop()

        recurse(0, 0, [])
        return solutions


s = Solution()
for combos, n in [(["((()))", "(()())", "(())()", "()(())", "()()()"], 3), (["()"], 1)]:
    actual = sorted(s.generateParenthesis(n))
    expected = sorted(combos)
    assert actual == expected, f"{n}: {actual} != {expected}"
