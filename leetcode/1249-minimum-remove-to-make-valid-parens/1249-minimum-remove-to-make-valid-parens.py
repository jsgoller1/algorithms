class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        output = []
        for c in s:
            if c == '(':
                output.append(c)
                balance += 1
            elif c == ')':
                if balance > 0:
                    output.append(c)
                    balance -= 1
            else:
                output.append(c)

        for i in range(len(output)-1, -1, -1):
            if balance > 0 and output[i] == '(':
                output[i] = ''
                balance -= 1

        return ''.join(output)


s = Solution()
for string, valids in [
    ("(a(b(c)d)", set(["a(b(c)d)", "(ab(c)d)", "(a(bc)d)"])),
    ("())()(((", set(["()()"])),
    ("", set([""])),
    ("((((((", set([""])),
    ("(())", set(["(())"])),
    ("))((", set([""])),
    ("lee(t(c)o)de)", set(["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"])),
    ("a)b(c)d", set(["ab(c)d"])),
]:
    result = s.minRemoveToMakeValid(string)
    assert result in valids, f"{string}: {result} not in {valids}"
