from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
- isbns are positive ints 
- LRU can be implemented with a queue
- hashing done with dict
- naive approach:
    - use queue and dict
    - whenever lookup/insert occurs, find item in queue, remove, and re-insert
    - if an item is ever outside the valid length of the queue, dequeue it and erase from dict
    - lookup, insert, and erase are O(n) where n is cache capacity. Can we achieve better? O(1)?
- If we keep an op counter, our "queue" could be implemented as a bst or sorted array? (no, we'd still
  have to shift)
- Could we use a doubly linked list? each dict entry has value and dll node pointer
    - have pointers newest and oldest, both start null
    - anytime something is updated, if other nodes were pointing to it, we clip it out and connect them
    - we then make it the newest
    - if we have to evict, we knock out the oldest and make its follower the new oldest
"""

from collections import OrderedDict


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.data = OrderedDict()
        self.capacity = capacity

    def _update_isbn(self, isbn):
        if isbn not in self.data:
            return
        price = self.data[isbn]
        del self.data[isbn]
        self.data[isbn] = price

    def lookup(self, isbn: int) -> int:
        if isbn not in self.data:
            return -1
        self._update_isbn(isbn)
        return self.data[isbn]

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.data:
            self._update_isbn(isbn)
            return
        self.data[isbn] = price
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)  # FIFO order

    def erase(self, isbn: int) -> bool:
        if isbn not in self.data:
            return False
        del self.data[isbn]
        return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
