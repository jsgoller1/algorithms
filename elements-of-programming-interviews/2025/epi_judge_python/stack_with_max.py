from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Use two actual stacks - each time a value is larger than the top, push it.
Each time a value is removed, if it matches the top of max, pop top of max.

Cases:
- empty
- Standard - random list of ints
- negatives, 0
- duplicate values (including of max) - nothing wrong with pushing them too 
"""

class Stack:
    def __init__(self):
        self.data = []
        self.maxes = []

    def empty(self) -> bool:
        return self.data == []

    def max(self) -> int:
        # Assuming 0 if stack empty
        return self.maxes[-1] if self.maxes else 0 

    def pop(self) -> int:
        # Assuming 0 if stack empty
        ret = self.data.pop() if self.data else 0 
        if self.maxes and ret == self.maxes[-1]:
            self.maxes.pop()
        return ret

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.maxes or x >= self.maxes[-1]:
            self.maxes.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
