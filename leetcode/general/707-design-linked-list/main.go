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
func (ll *MyLinkedList) AddAtHead(val int) {

}

// AddAtTail - Append a node of value val to the last element of the linked list.
func (ll *MyLinkedList) AddAtTail(val int) {

}

// AddAtIndex - Add a node of value val before the index-th node in the linked list.
// If index equals to the length of linked list, the node will be appended to the end
// of linked list. If index is greater than the length, the node will not be inserted.
// empty -> can only add at zero
// 1-2-3-4 -> add 8 at list[2] -> 1-2-8-3-4
func (ll *MyLinkedList) AddAtIndex(index int, val int) {

}

// DeleteAtIndex - Delete the index-th node in the linked list, if the index is valid.
func (ll *MyLinkedList) DeleteAtIndex(index int) {

}

func createLL(size int) *MyLinkedList {
	ll := Constructor()
	ll.head = &node{0, nil}
	curr := ll.head
	for i := 1; i < size; i++ {
		curr.next = &node{i * i, nil}
		curr = curr.next
		ll.len++
	}
	return &ll
}

func walkLL(ll *MyLinkedList) {
	curr := ll.head
	for i := 0; curr != nil; i++ {
		fmt.Println(i, curr)
		curr = curr.next
	}
}

func main() {
	/**
	 * Your MyLinkedList object will be instantiated and called as such:
	 * obj := Constructor();
	 * param_1 := obj.Get(index);
	 * obj.AddAtHead(val);
	 * obj.AddAtTail(val);
	 * obj.AddAtIndex(index,val);
	 * obj.DeleteAtIndex(index);
	 */
	ll := createLL(10)
	walkLL(ll)
	fmt.Println(ll.Get(4))
}
