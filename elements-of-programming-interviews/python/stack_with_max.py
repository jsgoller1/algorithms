from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.data = []
        self._maxes = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def max(self) -> int:
        return self._maxes[-1]

    def pop(self) -> int:
        if self.data[-1] == self._maxes[-1]:
            self._maxes.pop()
        return self.data.pop()

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self._maxes) == 0 or self.data[-1] >= self._maxes[-1]:
            self._maxes.append(x)


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
    """
    s = Stack()
    s.push(10)
    print(s.max())
    s.push(12)
    print(s.max())
    s.pop()
    print(s.max())

    """
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
