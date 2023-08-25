from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise RuntimeError(f"Queue must have at positive capacity (cannot use {capacity}).")
        self.capacity = capacity
        self.data = [""] * capacity
        self._size = 0
        self.tail = None
        self.head = None
        return

    def _resize(self, new_capacity):
        new_data = [""] * new_capacity
        head = self.head
        for i in range(self._size):
            new_data[i] = self.data[head]
            head = (head + 1) % self.capacity
        self.data = new_data
        self.capacity = new_capacity
        self.head = 0
        self.tail = self._size - 1

    def enqueue(self, x: int) -> None:
        if self._size == self.capacity:
            self._resize(self.capacity * 2)

        if self.tail == self.head == None:
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity

        self.data[self.tail] = x
        self._size += 1
        return

    def dequeue(self) -> int:
        if self._size == 0:
            raise RuntimeError("Cannot dequeue from empty queue.")
        val = self.data[self.head]
        self.data[self.head] = ""

        self._size -= 1
        if self._size == 0:
            self.tail = self.head = None
        else:
            self.head = (self.head + 1) % self.capacity
        return val

    def size(self) -> int:
        return self._size

    def __repr__(self):
        return f"Queue(capacity: {self.capacity}, size: {self._size}, tail: {self.tail}, head: {self.head}, {self.data})"


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
