/*
Statement

Design your implementation of the linked list. You can choose to use the singly
linked list or the doubly linked list. A node in a singly linked list should have
two attributes: val and next. val is the value of the current node, and next is a
pointer/reference to the next node. If you want to use the doubly linked list,
you will need one more attribute prev to indicate the previous node in the linked
list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:
- get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
- addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
- addAtTail(val) : Append a node of value val to the last element of the linked list.
- addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals
to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
- deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

Constraints:
- All values will be in the range of [1, 1000].
- The number of operations will be in the range of [1, 1000].
- Please do not use the built-in LinkedList library.
------------------------------------------------------------------------------------
Understand

- Cases
	-
------------------------------------------------------------------------------------
Plan / Pseudocode
------------------------------------------------------------------------------------
Execute / Review
*/
package main

import (
	"fmt"
)

type node struct {
	val  int
	next *node
}

// MyLinkedList represents the head of a linked list
type MyLinkedList struct {
	len  int
	head *node
	tail *node
}

// Constructor initializes your data structure . */
func Constructor() MyLinkedList {
	return MyLinkedList{0, nil, nil}
}

// Get - the value of the index-th node in the linked list. If the index is invalid, return -1.
// If index > len, return -1
// otherwise, walk list until we get to the index, then return that value
// called on an empty list returns -1
// called on any other list returns correct val
func (ll *MyLinkedList) Get(index int) int {
	fmt.Println("Getting ", index)
	if index > ll.len-1 || ll.len == 0 {
		return -1
	}
	curr := ll.head
	for i := 0; i < index; i++ {
		curr = curr.next
	}
	return curr.val
}

// AddAtHead - Add a node of value val before the first element of the linked list.
// After the insertion, the new node will be the first node of the linked list.
// Empty list -> new node becomes head and tail
// Nonempty -> new node becomes head
func (ll *MyLinkedList) AddAtHead(val int) {
	fmt.Println("Adding to head ", val)
	newNode := &node{val, nil}
	// list is empty if no head exists
	if ll.head == nil {
		ll.head = newNode
		ll.tail = newNode
	} else {
		newNode.next = ll.head
		ll.head = newNode
	}
	ll.len++
}

// AddAtTail - Append a node of value val to the last element of the linked list.
func (ll *MyLinkedList) AddAtTail(val int) {
	fmt.Println("Adding to tail ", val)
	newNode := &node{val, nil}
	// list is empty if no tail exists
	if ll.tail == nil {
		ll.tail = newNode
		ll.head = newNode
	} else {
		ll.tail.next = newNode
		ll.tail = newNode
	}
	ll.len++
}

// AddAtIndex - Add a node of value val before the index-th node in the linked list.
// If index equals to the length of linked list, the node will be appended to the end
// of linked list. If index is greater than the length, the node will not be inserted.
// empty -> can only add at zero
// 1-2-3-4 -> add 8 at list[2] -> 1-2-8-3-4
func (ll *MyLinkedList) AddAtIndex(index int, val int) {
	fmt.Println("Adding ", val, " at index ", index)
	if index > ll.len {
		return
	}

	if index == 0 {
		ll.AddAtHead(val)
	} else if index == ll.len {
		ll.AddAtTail(val)
	} else {
		curr := ll.head
		for i := 0; i < index-1; i++ {
			curr = curr.next
		}
		newNode := &node{val, curr.next}
		curr.next = newNode
		ll.len++
	}
}

// DeleteAtIndex - Delete the index-th node in the linked list, if the index is valid.
/*
empty list or invalid index:
	- return
one node list:
	- delete head and tail, return
multi-node list:
	deleting index(head):
		- head = head.next
		- size--
	deleting index(tail):
		- walk to node before tail
		- node.next = nil
		- tail = node
		- size--
	deleting middle index:
		- walk to node just before it
		- if node.next is tail, tail = node
		- node.next = node.next.next
*/
func (ll *MyLinkedList) DeleteAtIndex(index int) {
	fmt.Println("Deleting at index ", index)
	if index > ll.len-1 || ll.len == 0 {
		return
	} else if ll.len == 1 {
		ll.head = nil
		ll.tail = nil
	} else {
		if index == 0 {
			// deleting head
			ll.head = ll.head.next
		} else {
			// deleting tail or middle
			curr := ll.head
			for i := 0; i < index-1; i++ {
				curr = curr.next
			}
			if index == ll.len-1 {
				// deleting tail
				ll.tail = curr
				curr.next = nil
			} else {
				// deleting middle
				curr.next = curr.next.next
			}
		}
	}
	ll.len--
}

func createLL(size int) *MyLinkedList {
	ll := Constructor()
	if size == 0 {
		return &ll
	}

	ll.head = &node{0, nil}
	ll.tail = ll.head
	curr := ll.head
	for i := 1; i < size; i++ {
		curr.next = &node{i * i, nil}
		curr = curr.next
		ll.tail = curr
		ll.len++
	}
	return &ll
}

// Walk walks the linked list
func (ll *MyLinkedList) Walk() {
	curr := ll.head
	fmt.Println("----------------------------------------")
	fmt.Println(ll)
	for i := 0; curr != nil; i++ {
		fmt.Printf("%d: %p ", i, curr)
		fmt.Println(curr)
		curr = curr.next
	}
}

func main() {
	ll := Constructor()
	ll.AddAtHead(5) // 0 is 5
	ll.AddAtHead(2) // 0 is 2, 1 is 5
	ll.Walk()
	ll.DeleteAtIndex(1) // 0 is 2
	ll.Walk()
	/*
		ll.AddAtIndex(1, 9) // 0 is 2, 1 is 9
		ll.AddAtHead(4)     // 0 is 4, 1 is 2, 2 is 9
		ll.AddAtHead(9)     // 0 is 9, 1 is 4, 2 is 2, 3 is 9
		ll.AddAtHead(8)     // 0 is 8, 1 is 9, 2 is 4, 3 is 2, 4 is 9
		fmt.Println(ll.Get(3))
		ll.AddAtTail(1)
		ll.AddAtIndex(3, 6)
		ll.AddAtHead(3)
		ll.Walk()
	*/
}
