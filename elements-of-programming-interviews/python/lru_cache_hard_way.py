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


class QueueNode:
    def __init__(self, isbn, price):
        self.isbn = isbn
        self.price = price
        self.more = None
        self.less = None

    def __repr__(self):
        more = self.more.isbn if self.more else None
        less = self.less.isbn if self.less else None
        return f"QueueNode(isbn: {self.isbn}, price: {self.price}, more: {more}, less: {less})"


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.data = {}

    def __repr__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(repr(node))
            nodes.append("\n")
            node = node.less
            # print(f"repring node: {repr(node)}")
        return "".join(nodes)

    def _eviction_policy(self):
        if len(self.data) <= self.capacity:
            return
        if self.capacity == 0:
            self.head = None
            self.tail = None
            self.data = {}
        else:
            to_delete = self.tail
            self.tail = to_delete.more
            self.tail.less = None
            del self.data[to_delete.isbn]

    def _update_recency(self, node):
        if self.head == self.tail == None:
            # first node inserted
            self.head = node
            self.tail = node
            return

        if node == self.head:
            # Node is already most recent, nothing to do here
            return

        if node == self.tail:
            # If there's a node more recent than this one,
            # it becomes the new tail
            if node.more:
                self.tail = node.more
                self.tail.less = None

        if node != self.head and node != self.tail:
            # Ensure old more/less point to each other, if they exist
            if node.more:
                node.more.less = node.less
            if node.less:
                node.less.more = node.more

            # Bump previous head down if it existed and we weren't it.
            self.head.more = node
            node.less = self.head
            self.head = node
            node.more = None

    def lookup(self, isbn: int) -> int:
        if isbn not in self.data:
            # print(f"Lookup {isbn} (not found)")
            # print(f"{self.__repr__()}")
            return -1
        node = self.data[isbn]
        price = node.price
        self._update_recency(node)
        # print(f"Lookup {isbn}")
        # print(f"{self.__repr__()}")
        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.data:
            node = self.data[isbn]
        else:
            node = QueueNode(isbn, price)
            self.data[isbn] = node
        self._update_recency(node)
        self._eviction_policy()
        # print(f"Insert ({isbn},{price})")
        # print(f"{self.__repr__()}")

    def erase(self, isbn: int) -> bool:
        if isbn not in self.data:
            # print(f"Erase {isbn} (not found)")
            # print(f"{self.__repr__()}")

            return False

        node = self.data[isbn]
        if node.more:
            node.more.less = node.less
        if node.less:
            node.less.more = node.more

        if node == self.head:
            self.head = node.less
        if node == self.tail:
            self.tail = node.more

        del self.data[isbn]
        # print(f"Erase {isbn}")
        # print(f"{self.__repr__()}")
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
