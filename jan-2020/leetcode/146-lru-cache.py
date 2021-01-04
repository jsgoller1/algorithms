"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
                                 If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
    1 <= capacity <= 3000 (could be up to 3k items in the cache)
    0 <= key <= 3000 (keys could go up to 3k)
    0 <= value <= 10**4 (vals could go up to 10k)
    At most 30k calls will be made to get and put.
--------------------------
Regular cache:
    - Just use a python dictionary

Brute force (LRU with non constant put/get):
    - Use an array / queue where we shift each time an item is re-accessed
        - Either do a linear time lookup and constant time replacement, or constant time lookup and linear time replacement

Constant time put/get with hand-made DLL
    - Combine a doubly linked list with a dictionary
    - Dictionary stores the key->value association
    - Instantiate dict with pointer to head and tail
    - put() always puts elements at the head
    - Each time an element is get()'d, remove it from the list in O(1) time and insert it at the head
    - If we exceed allowed size, evict the tail; its prior element becomes the new tail
    - Do we need a DLL? Can we just use an SLL?
        - How would we evict in O(1) time? Pointer to tail becomes potentially impossible to update?
        - Also not sure how we'd move up in recency

    Methods:
        get()
            - missing: return -1, nothing else
            - head: return head's val, nothing else
            - middle: _make_most_recent(), return node's val
            - tail: _make_most_recent(), return node's val
        put()
            - empty: set new node to head and tail
            - capacity remaining: _make_most_recent(), add new node
            - full: add new node at head, _make_most_recent(), evict old tail node, remove from dictionary
                - Node doesn't store its key; how do we remove from dict? 
                    - Could have DLL nodes store k/v pairs; not sure how else to do this cleanly
            - duplicate key: _make_most_recent(), then update val

    Cases:
        - Capacity = 1
            - May have consequences for head/tail
        - Cap = >1

    Helper methods:
        _make_most_recent(node): moves a node to the head of the DLL, correctly updating references (including head/tail);
                            should not make any assumptions about cache capacity 

Constant time 
"""
# Leetcode doesn't allow this; otherwise we'd use DLL types in is constructor
#from __future__ import annotations


class DLLNode:
    def __init__(self, key: int = 0, val: int = 0, next_node=None, prev_node=None):
        self.key = key
        self.val = val
        self.next = next_node
        self.prev = prev_node


class LRUCache:
    def __init__(self, capacity: int):
        self._head = None
        self._tail = None
        self._cache = {}
        self._capacity = capacity

    def get(self, key: int) -> int:
        """
        - missing: return -1, nothing else
        - head: return head's val, nothing else
        - middle: _make_most_recent(), return node's val
        - tail: _make_most_recent(), return node's val
        """
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._make_most_recent(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        - duplicate key: _make_most_recent(), then update val
        - empty: set new node to head and tail
        - capacity remaining: _make_most_recent(), add new node
        - full: add new node at head, _make_most_recent(), evict old tail node, remove from dictionary
            - Node doesn't store its key; how do we remove from dict? 
                - Could have DLL nodes store k/v pairs; not sure how else to do this cleanly
        """
        if key in self._cache:
            node = self._cache[key]
            self._make_most_recent(node)
            node.val = value
        else:
            new_node = DLLNode(key, value)
            self._cache[key] = new_node
            cache_size = len(self._cache)

            if cache_size == 1:
                self.head = new_node
                self.tail = new_node
            else:
                self._make_most_recent(new_node)
                self._cache[key] = new_node

            if cache_size > self._capacity:
                key_to_remove = self.tail.key
                self.tail = self.tail.next
                self.tail.prev = None
                del self._cache[key_to_remove]

    def _make_most_recent(self, node: DLLNode) -> None:
        """
        _make_most_recent(node): moves a node to the head of the DLL, correctly updating references (including head/tail);
                    should not make any assumptions about cache capacity 
        """
        # Head is already most recent
        if node == self.head:
            return
        if node == self.tail:
            self.tail = self.tail.next

        # Remove node from old position:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Put node as new head:
        old_head = self.head
        old_head.next = node
        node.prev = old_head
        node.next = None
        self.head = node


if __name__ == '__main__':
    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(3, 2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2

    cache = LRUCache(2)
    cache.put(1, 1)  # cache is {1 = 1}
    cache.put(2, 2)  # cache is {1 = 1, 2 = 2}
    assert cache.get(1) == 1  # return 1
    cache.put(3, 3)
    assert cache.get(2) == -1  # returns -1 (not found)
    cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    assert cache.get(1) == -1  # return -1 (not found)
    assert cache.get(3) == 3  # return 3
    assert cache.get(4) == 4  # return 4
