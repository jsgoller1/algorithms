"""
This could be a graph search problem?
  - Root is []
  - In every step, the node is my stack state
  and the edges are the actions (push/pop).
    - Graph is a binary tree
  - We can take the push action only if pushed is nonempty.
  - We can take the pop action only if the top of the stack is equal to pop[0]
---------------------------------------------
- Modified graph search:
  - Start with stack = [], push / pop = to inputs
  - while pushed and popped
    - if stack and popped[0] == stack[-1]:
      stack.pop()
      popped = popped[1:]
    - elif pushed:
      stack.append(pushed[0])
      pushed = pushed[1:]
    - else:
      return False
  - return True
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        while pushed or popped:
            if stack and popped[0] == stack[-1]:
                stack.pop()
                popped = popped[1:]
            elif pushed:
                stack.append(pushed[0])
                pushed = pushed[1:]
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False
    assert s.validateStackSequences([], []) == True
