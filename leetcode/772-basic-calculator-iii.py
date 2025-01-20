from collections import deque 
from string import digits

class Solution:
    def tokenize(self, s):
        tokens = deque([])
        curr_int = []
        for c in s:
            if c in digits:
                curr_int.append(c)
            else: 
                if curr_int:
                    tokens.append(int(''.join(curr_int)))
                    curr_int = []
                tokens.append(c)
        if curr_int:
            tokens.append(int(''.join(curr_int)))
        return tokens 

    def div_mult_pass(self, tokens):
        def div(x,y):
            neg = (x < 0) ^ (y < 0)
            x, y = abs(x), abs(y)
            return (x // y) * (-1 if neg else 1)

        operators = {
            "/": div,
            "*": lambda x,y: x * y,
        }
        return self.binary_operator_pass(tokens, operators)

    def add_sub_pass(self, tokens):
        operators = {
            "-": lambda x,y: x - y,
            "+": lambda x,y: x + y,
        }
        return self.binary_operator_pass(tokens, operators)

    def binary_operator_pass(self, tokens, operators):
        stack = deque([])
        while tokens:
            token = tokens.popleft() 
            if token == '(':
                result = self.execute_passes(tokens)
                tokens.appendleft(result[0])
            elif token == ')':
                break
            elif isinstance(token, int) and stack and stack[-1] in operators:
                operator, left, right = stack.pop(), stack.pop(), token
                stack.append(operators[operator](left, right))
            else:
                stack.append(token)
        return stack


    def execute_passes(self, tokens):
        tokens = self.div_mult_pass(tokens)
        tokens = self.add_sub_pass(tokens)
        return tokens

    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        return self.execute_passes(tokens)[0]

s = Solution()
for expr, expected in [
    ("1+1", 2),
    ("6-4/2", 4),
    ("2*(5+5*2)/3+(6/2+8)", 21),
    ("(0-3)/4", 0)
]:
    actual = s.calculate(expr)
    assert actual == expected, f"{expr}: {actual} != {expected}"