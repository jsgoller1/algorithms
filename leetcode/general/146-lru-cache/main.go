/*
Statement

Design and implement a data structure for Least Recently Used (LRU)
cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not
already present. When the cache reached its capacity, it
should invalidate the least recently used item before
inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2  ); // 2 is capacity
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Input: A sequence of calls to get/put
Outpt: Expected return values of each function (if any)

Constraints:
	- Keys will always be positive
--------------------------------------------------------
Understand
- Starting off with linear time solution, then getting a constant time one
- the get and set operations work like a normal hash table;
we should be able to get() and set() like normal.
- For LRU, we need to keep an internal cache clock
	- every operation (reads and writes) should update the clock
	- when we write a value, we check first if the key is already present;
	if so, update its value. If not, evict the least recently used value
	and replace it.
- If we maintain an internal clock, finding the LRU entry will be O(N)
if we scan the table each time; we need a way to find the entry in O(1)
time.

- For a constant time set, we need a way of keeping the operation
times ordered; if we evict the least recently used entry, we need to
figure out in O(1) what the next-least-recently-used entry is. Some
constant time operations:
	- Appending / removing the the first/last entry from a linked list
	- Hashing a value
	- WHY NOT BOTH?
- We can store the k,v pairs instead as k,node pairs; each node
is a node in a doubly linked list.
- Keep track of list head and tail
- We do our sets and gets in the hashtable as normal. For updating
	recency, we have the following cases:
	- Inserting a new node
		- List was empty
		- List was nonempty
	- Updating an existing node
		- Node was the head
			- quit, already most recent
		- Node was the tail
			- tail.next becomes tail, tail.prev is old head, tail.next is null, tail becomes head
	- Node was in the middle
		- prev.next = node.next, next.prev = node.prev, node.prev = head, head.next = node, head = node


--------------------------------------------------------
Plan / Pseudocoding

- we are going to pretend that Go's map lookup is never worse
than O(1), which it probably is for some cases.

cache:
	map int->int (cache)
	map int->int (timestamps)
	int currentTime

O(1) get
get(k):
	currentTime++
	if k in cache:
		timestamps[k] = currentTime // this will assign timestamps for nil values!
		return cache[k]
	else:
		return -1

O(N) set
set(k, v):
	if cache.full():
		lruK = nil
		minTs = inf
		for k in cache.keys():
			if timestamps[k] < minTs:
				minTs = timestamps[k]
				lruK = k
		evict(k)
	currentTime++
	timestamps[k] = currentTime
	cache[k] = v


--------------------------------------------------------
Execute

See below
--------------------------------------------------------
Review

- Didn't think about all the possible ways to use get()
and set(); missed a case where we set() an existing value
in a full cache (shouldn't cause an eviction)
*/
package main

import (
	"fmt"
)

// LRUCacheNode is a doubly linked list node for our LRU cache
type LRUCacheNode struct {
	key  int
	val  int
	prev *LRUCacheNode
	next *LRUCacheNode
}

// LRUCache implements Least Recently Used caching
type LRUCache struct {
	table    map[int]LRUCacheNode
	capacity int
	head     *LRUCacheNode
	tail     *LRUCacheNode
}

// Constructor creates an LRUCache
func Constructor(capacity int) LRUCache {
	ht := make(map[int]LRUCacheNode, capacity)
	return LRUCache{ht, capacity, nil, nil}
}

func (cache *LRUCache) dumpInfo(message string) {
	fmt.Println(message)
	fmt.Printf("%p ", cache.head)
	fmt.Println("Head: ", cache.head)
	fmt.Printf("%p ", cache.tail)
	fmt.Println("Tail: ", cache.tail)
	for key, val := range cache.table {
		fmt.Printf("%p ", &val)
		fmt.Println(key, val)
	}
	fmt.Println()
}

func (cache *LRUCache) handleNewNode(node *LRUCacheNode) {
	if len(cache.table) == 1 {
		// no previous tail, become tail
		cache.tail = node
		fmt.Printf("%p %p\n", node, cache.tail)
	} else {
		node.prev = cache.head
		cache.head.next = node
	}
	cache.head = node
	cache.dumpInfo("handled new")
}

func (cache *LRUCache) updateExistingNode(node *LRUCacheNode) {
	if node == cache.head {
		return
	} else if node == cache.tail {
		cache.tail = cache.tail.next
		cache.tail.prev = nil
	} else {
		node.prev.next = node.next
		node.next.prev = node.prev
	}
	node.prev = cache.head
	node.next = nil
	cache.head.next = node
	cache.head = node
	cache.dumpInfo("updated existing")
}

func (cache *LRUCache) evictOldestNode() {
	oldest := cache.tail
	if len(cache.table) == 1 {
		cache.head = nil
		cache.tail = nil
	} else {
		cache.tail = cache.tail.next
		cache.tail.prev = nil
	}
	delete(cache.table, oldest.key)
	cache.dumpInfo("eviction")
}

// Get retrieves a key from an LRU cache
func (cache *LRUCache) Get(key int) int {
	node, present := cache.table[key]
	if !present {
		return -1
	}

	cache.updateExistingNode(&node)
	return node.val
}

// Put sets a key in an LRU cache
func (cache *LRUCache) Put(key int, value int) {
	node, present := cache.table[key]
	if len(cache.table) == cache.capacity && !present {
		cache.evictOldestNode()
	}

	if present {
		node.val = value
		fmt.Println(node)
		cache.updateExistingNode(&node)
	} else {
		newEntry := LRUCacheNode{key: key, val: value, prev: nil, next: nil}
		cache.table[key] = newEntry
		cache.handleNewNode(&newEntry)
	}
}

func main() {
	cache := Constructor(2)
	//cache.Get(2)
	cache.Put(2, 6)
	//cache.Get(1)
	//cache.Put(1, 5)
	//cache.Put(1, 2)
	//cache.Get(1)
	//cache.Get(2)
}
