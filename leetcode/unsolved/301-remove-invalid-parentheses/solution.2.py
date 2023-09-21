"""
- we can keep valid strings in a set (though it'd be better not to compute duplicates wastefully)
- only want valid strings with minimum removals
- when we read an invalid string, how many ways are there to make it valid?
    - (() and ()): we can delete mismatching, both result in the same. 
    

- ((()(())

"""


from collections import deque
from typing import List


def prune(s: str):
    pruned = deque(s)

    i = 0
    while i < len(pruned) and pruned[i] != '(':
        if pruned[i] == ')':
            pruned[i] = ''
        i += 1

    i = len(pruned)-1
    while 0 <= i and pruned[i] != ')':
        if pruned[i] == '(':
            pruned[i] = ''
        i -= 1
    return [char for char in pruned if char]


def get_paren_counts(s: deque):
    closers = openers = 0
    for c in s:
        if c == "(":
            openers += 1
        if c == ")":
            closers += 1
    return openers, closers


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        arr = prune(s)
        valid_strings = set([])

        def dfs(stack, i, balance):
            # Base cases: no more characters left
            if i == len(arr):
                if stack and balance == 0:
                    valid_strings.add("".join(stack))
                return
            # Base case: no way to make valid string
            if balance < 0:
                return

            delta = 0
            delta += -1 if arr[i] == ")" else 0
            delta += 1 if arr[i] == "(" else 0
            # Recursive cases
            if balance + delta >= 0:
                dfs(stack + [arr[i]], i+1, balance + delta)
            dfs(stack, i+1, balance)

        dfs([], 0, 0)
        return [s for s in valid_strings]


s = Solution()
cases = [
    # ("())(((()m)(", ["()(()m)"]),
    ("))(()(", ["()"]),
    ("((i)", ["(i)"]),
    ("", [""]),
    (")(", [""]),
    ("()())()", ["(())()", "()()()"]),
    ("(a)())()", ["(a())()", "(a)()()"]),
    ("n", ["n"]),
    ("(()", ["()"]),
]
for i, case in enumerate(cases):
    in_string, expected = case
    actual = s.removeInvalidParentheses(in_string)
    assert set(expected) == set(actual), f"{i}: {in_string}: {actual} != {expected}"
