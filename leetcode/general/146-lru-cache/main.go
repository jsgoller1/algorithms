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

- Starting off with linear time solution, then getting a constant time one

--------------------------------------------------------
Plan / Pseudocoding

- we are going to pretend that Go's map lookup is never worse
than O(1), which it probably is for some cases.

cache:
	map int->int (cache)
	map int->int (timestamps)
	int currentTime

get(k):
	currentTime++
	if k in cache:
		timestamps[k] = currentTime // this will assign timestamps for nil values!
		return cache[k]
	else:
		return -1

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
*/
package main

import (
	"fmt"
)

// LRUCache implements Least Recently Used caching
type LRUCache struct {
	ht         map[int]int
	timestamps map[int]int
	time       int
	capacity   int
}

// Constructor creates an LRUCache
func Constructor(capacity int) LRUCache {
	ht := make(map[int]int, capacity)
	timestamps := make(map[int]int, capacity)
	return LRUCache{ht, timestamps, 0, capacity}
}

// Get retrieves a key from an LRU cache
func (cache *LRUCache) Get(key int) int {
	cache.time++
	v, present := cache.ht[key]
	if !present {
		return -1
	}
	cache.timestamps[key] = cache.time
	return v
}

// Put sets a key in an LRU cache
func (cache *LRUCache) Put(key int, value int) {
	cache.time++
	_, present := cache.ht[key]
	if len(cache.ht) == cache.capacity && !present {
		leastRecentTime := cache.time
		leastRecentKey := key
		for k := range cache.ht {
			if cache.timestamps[k] < leastRecentTime {
				leastRecentTime = cache.timestamps[k]
				leastRecentKey = k // if the cache is full, this must happen at least once
			}
		}
		delete(cache.ht, leastRecentKey)
		delete(cache.timestamps, leastRecentKey)
	}
	cache.timestamps[key] = cache.time
	cache.ht[key] = value
}

func main() {
	cache := Constructor(2)
	fmt.Println(cache.Get(2))
	cache.Put(2, 6)
	fmt.Println(cache.Get(1))
	cache.Put(1, 5)
	cache.Put(1, 2)
	fmt.Println(cache.Get(1))
	fmt.Println(cache.Get(2))

	fmt.Println(cache)
}
