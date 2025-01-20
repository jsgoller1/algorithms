from collections import deque
from string import digits

class Solution:
    def tokenize(self, string):
        tokens = deque([])
        curr_int = []
        for c in string:
            if c == ' ':
                continue
            elif c in digits:
                curr_int.append(c)
            else: 
                if curr_int:
                    tokens.append(int(''.join(curr_int)))
                    curr_int = []
                tokens.append(c)

        if curr_int:
            tokens.append(int(''.join(curr_int)))
        return tokens
    
    def evaluate(self, tokens):
        stack = []
        while tokens: 
            token = tokens.popleft()
            if token in ['+', '-']:
                stack.append(token)
            elif token == '(':
                tokens.appendleft(self.evaluate(tokens))
            elif token == ')':
                break 
            else: # token is an int:
                if not stack:
                    stack.append(token)
                elif stack[-1] == '+':
                    _, token2, = stack.pop(), stack.pop()
                    stack.append(token2 + token)
                elif stack[-1] == '-' and len(stack) == 1:
                    stack.pop()
                    stack.append(-1 * token)
                else:
                    _, token2, = stack.pop(), stack.pop()
                    stack.append(token2 - token)
        return stack[0] if stack else 0

    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        return self.evaluate(tokens)

s = Solution()
for expr in [
    "1 + 1",
    " 2-1 + 2 ",
    "(1+1)",
    "-5",
    "-(10)",
    "(1+(4+5+2)-3)+(6+8)"
]:
    actual = s.calculate(expr)
    expected = eval(expr)
    assert actual == expected, f"{expr}: {actual} != {expected}"