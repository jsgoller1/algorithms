"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
=====================
Input: String of delimiters
Output: Bool

- This is a stacks problem; you can solve it for just parens
but pushing every time an open paren occurs and popping every
time a close paren occurs; popping from an empty stack or having
a nonempty stack at the end means the string is invalid

- An expression like "{(})" is not valid, so we shouldn't
try using "multiple stacks" with the same approach
- If we put everything the _same_ stack, though, we can confirm on pop
that we are popping the correct character. When we encounter ")" in "{()}",
we'd pop "(", so it's valid. However in {(})", when we encounter "}", we pop "("
which is invalid.
-----------------------------
pseudo(string):
  - stack = stack()
  - for each character in the string:
    - if {, (, or [, push it onto the stack
    - if }, ), or ], pop from the stack. If stack is empty
    or popped character doesn't match, return false.
  - return true if stack is empty, false if not
"""


class Solution(object):
    def isValid(self, s):
        openers = ["[", "(", "{"]
        closers = ["]", ")", "}"]
        stack = []
        for char in s:
            if char in openers:
                stack.append(char)
            elif char in closers and stack:
                matchChar = stack.pop()
                if openers.index(matchChar) != closers.index(char):
                    return False
            else:
                return False

        return stack == []


if __name__ == '__main__':
    s = Solution()
    assert s.isValid("]") == False
    assert s.isValid("") == True
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
    assert s.isValid("{[]}") == True
