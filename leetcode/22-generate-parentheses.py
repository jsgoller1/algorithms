import itertools

"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

---
Understand

In this question, we must generate lists of valid parenthetical expressions. A parenthetical
expression is valid if every open paren has a closing paren:

Valid:
()
()()
(())
()(())

Invalid:
())
)
)))

In: n, int
Out: list of strings

---
Plan

You can validate a parenthetical expression using a stack; parse the string, pushing
open parens onto the stack and popping each time a closing paren is found. If by the end of
the expression the stack is empty, the expression is valid. If non-empty, it is invalid.

There's a couple ways we can handle this problem:
- Brute force: create an array, append n many open parens and n many closed parens to it,
generate all permutations of this array, turn them into strings, and validate each one.
- Backtracking: base case - n many closed and open parens are in the string; validate and
save if valid, otherwise recurse by adding each type of character.
- Binary: Given a bit-string of length n*2, assume that a 1 represents an open paren and
a 0 represents a close paren. Then loop through all string from 000...0 to 111...1 and
save valid ones. We can ignore all cases where the number of 1s is not equal to the number
of zeros. There's a neat way to quickly test this from K&R:

We will start with the brute force approach.
---
Execute

See below.
---
Review

Time to solve: 40m (~15m of planning, ~10m for each solution; brute force was faster to develop)

The backtracking solution actually was quite fast to develop - I was surprised at how slow the
brute force solution's performance became at n > 6!
"""


def is_valid(expr):
    """
    Test a parenthetical expression
    using a stack.
    """
    s = []
    try:
        for each in expr:
            if each == '(':
                s.append(each)
            else:
                s.pop()
    except IndexError:
        return False
    else:
        return not s


class Solution:
    def bf_generateParenthesis(self, n):
        """
        Generate all parenthetical expressions
        by brute forcing through all permutations.
        This is extremely slow.

        :type n: int
        :rtype: List[str]
        """
        parens = (['('] * n) + ([')'] * n)
        expressions = []
        for combo in itertools.permutations(parens):
            expr = ''.join(combo)
            if expr not in expressions:
                expressions.append(expr)
        return [expr for expr in expressions if is_valid(expr)]

    def generateParenthesis(self, n):
        """
        Generate all permutations via backtracking. This works
        much faster.

        :type n: int
        :rtype: List[str]
        """
        self.valid_exprs = []
        self.solve('', l_paren=n, r_paren=n)
        return self.valid_exprs

    def solve(self, expr, *, l_paren, r_paren):
        """
        Recursive backtracking solution.
        """
        # Test base case
        if l_paren == r_paren == 0:
            if is_valid(expr):
                return True
            else:
                return False
        if l_paren < 0 or r_paren < 0:
            return False

        # Try different kinds of parens
        if self.solve(expr + '(', l_paren=l_paren - 1, r_paren=r_paren):
            self.valid_exprs.append(expr + '(')
        if self.solve(expr + ')', l_paren=l_paren, r_paren=r_paren - 1):
            self.valid_exprs.append(expr + ')')


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
