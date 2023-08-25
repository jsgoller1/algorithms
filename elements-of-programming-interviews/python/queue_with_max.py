from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
- max stack uses separate stack
- queue adds to end, releases from front. 
- any time we add to the end, the max can change; 
  any time we release from front, too
- likely not viable in O(c) time and space

- use a deque
- each time we find a new max, dump the old deque, start with 
  just current element
- if we enqueue something less than current max, enqueue to deque
- if the dequeued item matches current max, pop from deque
"""

import collections


class QueueWithMax:
    def __init__(self):
        self.data = collections.deque()
        self.max_vals = collections.deque()

    def enqueue(self, x: int) -> None:
        self.data.appendleft(x)
        if not self.max_vals:
            self.max_vals.append(x)
            return

        if x > self.max_vals[-1]:
            self.max_vals = collections.deque([x])
        else:
            while self.max_vals[0] < x:
                self.max_vals.popleft()
            self.max_vals.appendleft(x)

    def dequeue(self) -> int:
        if self.data[-1] == self.max_vals[-1]:
            self.max_vals.pop()
        return self.data.pop()

    def max(self) -> int:
        return self.max_vals[-1]

    def __repr__(self):
        return f"QueueWithMax(data: {self.data}, maxes: {self.max_vals})"


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
