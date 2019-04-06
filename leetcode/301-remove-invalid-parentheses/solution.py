"""
Remove the minimum number of invalid parentheses in order to
make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]

Example 4:
Input: "(()"
Output: ["()"]

Example 5:
Input: "(()()"
Output: ["()()", "(())"]
-------------------------------------------------------------
Input: string
Output: list[string]

- We can use the stack-based method to determine whether the
  string is invalid or not. This requires O(n) time.
- Why might an expression be invalid?
  - if at any point in an expression we find more closers than openers; this can
    never be corrected by later parens.
  - if at the end of an expression, we have not encountered sufficient closers;
    finding an opener mid string can be resolved by following characters.
- Using a brute force approach, we could try all possible strings with 1 character
  deleted, then recursively do this on each string. As soon as we found a valid
  string with n characters deleted, we only need to finish looking for other strings
  with n characters deleted and then return them. This will devolve into factorial
  complexity, so it won't work for large strings. This would be better if we could
  delete problematic characters
- We can find which specific characters render a string invalid by keeping
  tuples of (i, char); if we pop an empty stack, push a bad ")", and
  if the stack is nonempty once parsing ends, each "(" is bad.
  However, just deleting these characters isn't enough because there
  will be other characters we can remove that render a valid, equal
  length string.
- Using the previous point, can we recover and count the minimum number
  of deletions that must occur? If we count each time an empty pop
  happens plus each paren left on the stack as k, then there
  are at most len choose k many valid strings, and not all of them
  are valid.
- If we have an invalid closing paren, should we only look at it
  and left of it to determine which parens to delete? As we look for
  valid expressions, we should consider using a set.
- Looked at related topics, which just had "BFS" and "DFS"; how could
  we apply graph search? My recursive function above is like a tree search,
  but the complexity is len-1 * len-2 * len-3 * ... len - len
- Once we know a single solution, we can store that as the maximum depth we need to go;
  if we find a single-deletion result, we can ignore any 2+ deletions.
-----------------------------------------------------------------------------------
- Our strategy will be:
  - Have a linear-time validate() function
  - Execute a BFS; nodes are char strings, edges are deletions, root is original expression,
    target is the first valid expression we find.
  - Once we find a valid expression, we set a minLen variable (originally initialized to
   infinity) to its length; moving forward, we reject any possible nodes that are shorter
   than minLen
  - We should keep a visited set to avoid unnecessary reprocessing.
  - I _STRONGLY_ expect this to TLE; if we have a 100-character string that needs 50 chars
    removed, we are in trouble. Even with a visited set, we are looking at 2^n possible nodes
    in the worst case.
---------------------------------------------------------
- Initial attempt works on all cases but I will be very surprised if it doesn't TLE.
- It TLE'd on "()(((((((()"; looks like I forgot to utilize the visited set despite
creating it.
- Using the visited set, the pathological edge case goes from 12s to 20ms
Dang, it actually worked (in 800ms)
"""
import collections


class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return stack == []

    def removeInvalidParentheses(self, s):
        maxEdits = float('inf')
        visited = set()
        solutions = set()
        q = collections.deque([(0, list(s))])
        while q:
            editCount, expression = q.popleft()
            if maxEdits < editCount or ''.join(expression) in visited:
                continue
            if self.isValid(expression):
                maxEdits = editCount
                solutions.add(''.join(expression))
            # we will wind up removing chars we don't need to
            # TODO: Find problem chars, bfs from there
            for i, char in enumerate(expression):
                if char in ['(', ')']:
                    q.append(
                        (editCount + 1, expression[:i] + expression[i + 1:]))
            visited.add(''.join(expression))

        return list(solutions)


s = Solution()
cases = [
    ["()(()", ["()()"]],
    ["(())(()", ["(())()"]],
    ["()())()", ["()()()", "(())()"]],
    ["(a)())()", ["(a)()()", "(a())()"]],
    [")(", [""]],
    ["", [""]],
    ["()(((((((()", ["()()"]]
]
for case in cases:
    print("-"*10)
    arg, expected = case[0], set(case[1])
    actual = set(s.removeInvalidParentheses(arg))
    print("actual: {0}, expected {1}".format(actual, expected))
    assert actual == expected
