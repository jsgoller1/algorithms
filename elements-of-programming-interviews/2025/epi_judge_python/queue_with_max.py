from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque

class QueueWithMax:
    def __init__(self):
        self.data = deque()
        self.maxes = deque()

    def enqueue(self, x: int) -> None:
        self.data.append(x)
        while self.maxes and self.maxes[-1] < x:
            self.maxes.pop()
        self.maxes.append(x)

    def dequeue(self) -> int:
        if (self.data and self.maxes) and (self.data[0] == self.maxes[0]):
            self.maxes.popleft()
        return self.data.popleft()

    def max(self) -> int:
        return self.maxes[0] if self.maxes else 0


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
