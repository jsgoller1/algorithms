def push(stack, token):
    if token == "":
        return
    if token not in ["+", "-"]:
        token = int(token)
    if len(stack) == 1 and stack[0] == "-":
        stack.pop()
        token *= -1
    if len(stack) == 2:
        oper = stack.pop()
        op1 = int(stack.pop())
        op2 = int(token)
        token = op1 + op2 if oper == "+" else op1 - op2
    stack.append(token)


def pop(stack):
    return stack.pop() if stack else None


def _calculate(s: str, i: int = 0) -> (int, int):
    stack = []
    token = ""
    while i < len(s):
        if s[i] == '(':
            val, i = _calculate(s, i+1)
            push(stack, val)
        elif s[i] == ')':
            push(stack, token)
            return pop(stack), i+1
        elif s[i] in ['+', '-']:
            push(stack, token)
            push(stack, s[i])
            token = ""
            i += 1
        elif s[i] == " ":
            i += 1
        else:
            token += s[i]
            i += 1

    push(stack, token)
    return pop(stack), i


class Solution:
    def calculate(self, s: str) -> int:
        return _calculate(s)[0]


s = Solution()
cases = [
    "(7)-(0)+(4)",
    "-2+ 1",
    "-(2+1)",
    "2+(-1)",
    "2-(-1)",
    "11",
    "1 + 1",
    " 2-1 + 2 ",
    "(1+2)",
    "(1+2)+3",
    "((1+2)+3)+4",
    "(1+(4+5+2)-3)+(6+8)",
    # "()",
    # "(())",
    "(11)",
]
for expr in cases:
    assert s.calculate(expr) == eval(expr), f"{expr}: {eval(expr)} != {s.calculate(expr)}"
