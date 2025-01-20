from test_framework import generic_test
from test_framework.test_failure import TestFailure


class DLLNode:
    def __init__(self, isbn, price):
        self.isbn = isbn
        self.price = price 
        self.next = None 
        self.prev = None 

    def __repr__(self):
        return f"[{self.isbn},{self.price},{self.next.isbn if self.next else None}, {self.prev.isbn if self.prev else None}]"

from collections import OrderedDict

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity 
        self.data = OrderedDict()

    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self.data:
            self.data[isbn] = price 
        self.data.move_to_end(isbn, last=False)
        if len(self.data) > self.capacity:
            self.data.popitem()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.data:
            return -1
        self.data.move_to_end(isbn, last=False)
        return self.data[isbn] 

    def erase(self, isbn: int) -> bool:
        if isbn not in self.data:
            return False 
        del self.data[isbn]
        return True  

class LruCacheManual:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity 
        self.map = {}
        self.head = None 
        self.tail = None 

    # Queue methods
    def _pop_tail(self):
        self.tail = self.tail.next
        self.tail.prev = None 

    def _push_head(self, node):
        self.head.next = node 
        node.prev = self.head 
        self.head = node 

    def _fixup_neighbors(self, node):
        if node.next:
            node.next.prev = node.prev 
        if node.prev:
            node.prev.next = node.next 

    def _remove_node(self, node):
        if node == self.head == self.tail:
            self.head = self.tail = None  
        elif node == self.head:
            self.head = node.prev 
            self.head.next = None 
        elif node == self.tail:
            self._pop_tail()
        else:
            self._fixup_neighbors(node)

    def _eviction_policy(self):
        if len(self.map) <= self.capacity:
            return 
        to_delete = self.tail
        del self.map[self.tail.isbn]
        self._remove_node(self.tail)

    def _update_recency(self, node):
        # Occurs when map is empty 
        if not (self.head and self.tail):
            self.head = self.tail = node 
            return 
        if node == self.head:
            return 
        if node == self.tail:
            self._pop_tail()
        self._fixup_neighbors(node)
        self._push_head(node)

    # Cache methods 
    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self.map:
            node = DLLNode(isbn, price)
            self.map[isbn] = node
        self._update_recency(self.map[isbn])
        self._eviction_policy()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.map:
            return -1 
        self._update_recency(self.map[isbn])
        return self.map[isbn].price

    def erase(self, isbn: int) -> bool:
        if isbn not in self.map:
            return False 
        self._remove_node(self.map[isbn])
        del self.map[isbn]
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
