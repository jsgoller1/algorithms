from string import digits 

OPERATORS = ['-', '+', '/', '*']

class Solution:
    def tokenize(self, s):
        tokens = []
        curr_int = []
        for c in s: 
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

    def binary_operator_pass(self, tokens, methods):
        stack = []
        for token in tokens:
            if isinstance(token, int) and stack and stack[-1] in methods:
                operator = stack.pop()
                token2 = stack.pop()
                stack.append(methods[operator](token2, token))
            else:
                stack.append(token)
        return stack


    def mult_div_pass(self, tokens):
        methods = {
            "/": (lambda x, y: x // y),
            "*": (lambda x, y: x * y),
        }
        return self.binary_operator_pass(tokens, methods)

    def add_sub_pass(self, tokens): 
        methods = {
            "-": (lambda x, y: x - y),
            "+": (lambda x, y: x + y),
        }
        return self.binary_operator_pass(tokens, methods)

    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        tokens = self.mult_div_pass(tokens)
        return self.add_sub_pass(tokens)[0]


s = Solution()
for expr, expected in [
     ("3+2*2", 7),
     (" 3/2 ", 1),
     (" 3+5 / 2 ", 5),
]:
    actual = s.calculate(expr)
    assert actual == expected, f"{expr}: {actual} != {expected}"