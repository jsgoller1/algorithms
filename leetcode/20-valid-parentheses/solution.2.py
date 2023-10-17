class Solution:
    def isValid(self, s: str) -> bool:
        closers = {'}': '{', ')': '(', ']': '['}
        openers = ['(', '{', '[']
        stack = []

        for c in s:
            if c in openers:
                stack.append(c)
            elif (not stack) or stack[-1] != closers[c]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
