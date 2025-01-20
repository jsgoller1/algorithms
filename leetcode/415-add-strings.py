from collections import deque


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digits1 = [int(digit) for digit in num1]
        digits2 = [int(digit) for digit in num2]
        carry = 0
        sol = deque([])
        while digits1 or digits2:
            d1 = digits1.pop() if digits1 else 0
            d2 = digits2.pop() if digits2 else 0
            total = carry + d1 + d2
            carry = 1 if total >= 10 else 0
            sol.appendleft(str(total % 10))
        if carry:
            sol.appendleft("1")
        return ''.join(sol)


s = Solution()
for s1, s2, expected in [
    ("1", "1", "2"),
    ("9", "1", "10"),
    ("0", "0", "0"),
    ("0", "9", "9"),
    ("11", "123", "134"),
    ("456", "77", "533")
]:
    actual = s.addStrings(s1, s2)
    assert actual == expected, f"{s1} + {s2} = {expected}, not {actual}"
