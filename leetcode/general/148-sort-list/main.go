/*
Statement

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

Constraints:
- Not explicitly stated, but examples are lists of ints,
and Val is an int.
---------------------------
Understand

Cases:
- Empty list
	- Return nil
- Single node list
	- We will say this is implicitly sorted and return as is
- Multiple nodes
	- Unsorted
	- Sorted

- Solution must be O(N*log(N)), which means that we can
do a constant number of O(N) operations.
- Can't use a list / additional structure
- If it's linearithmic time, maybe we should be dividing and conquering?
	- could we progressively examine half of the linked list until we have one node, like
		merge sort?
	- We could walk the list once to get the length; from then on, we can divide and not need to
	re-walk the new list.
	- we could then do something like a mergesort

---------------------------
Plan / Pseudocode
- walk list once to get length
- mergesort(list, len)

// is this actually nlogn? Skiena says that "doing half of something each time" is log(n), but
// we are traversing a singly linked list
mergesort(list, len)
- if list len == 1: return
- else:
	- walk to midway of first half of list
	- call mergesort(node, len/2) on second half
	- set next of last node in first half to nil
	- call mergesort(list, len/2) on first half (original list reference)
	 - merge() first half and second half, return merged

merge(list1, list2):
	- newlist listpointer
	while left and right are not nil
	if left is nil:
		remove first node from right, add it to new list
	if right is nil:
		remove first node from left, add it to new list
	else
		add greater of left or right to new list, remove it from previous list
	return merged list

- we can have an if-guard that if list is nil, return list
- if above is called one 1 node list, it just returns that node
- even length lists are the expected case
- for odd length lists greater than 1, divide len by 2, round up to get k, and call mergesort on first half with len k and second half with k-1
- later on we could add an isSorted() method to walk and determine if the list is already sorted; this will be an optimization
---------------------------
Execute / Review

*/
package main

import (
	"fmt"
)

// ListNode defines a node in a singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Walk walks the linked list
func Walk(ll *ListNode) {
	fmt.Println("----------------------------------------")
	for i := 0; ll != nil; i++ {
		fmt.Printf("%d: %p ", i, ll)
		fmt.Println(ll)
		ll = ll.Next
	}
	fmt.Println("----------------------------------------")
}

func createLL(size int, isSorted bool) *ListNode {
	if size == 0 {
		return nil
	}

	ll := &ListNode{0, nil}
	curr := ll
	for i := 1; i < size; i++ {
		var val int
		if isSorted {
			val = i
		} else {
			val = i * i
			if i%2 == 0 {
				val *= -1
			}
		}
		newNode := ListNode{val, nil}
		curr.Next = &newNode
		curr = curr.Next
	}
	return ll
}

// Len gets the length of the list
func Len(ll *ListNode) int {
	if ll == nil {
		return 0
	}

	var length int
	for length = 0; ll != nil; length++ {
		ll = ll.Next
	}
	return length
}

func merge(head1, head2 *ListNode) *ListNode {
	var mergedList *ListNode
	if head1.Val <= head2.Val {
		mergedList = head1
		head1 = head1.Next
	} else {
		mergedList = head2
		head2 = head2.Next
	}

	curr := mergedList
	for head1 != nil && head2 != nil {
		if head1.Val <= head2.Val {
			curr.Next = head1
			head1 = head1.Next
		} else {
			curr.Next = head2
			head2 = head2.Next
		}
		curr = curr.Next
	}

	if head1 != nil {
		curr.Next = head1
	} else if head2 != nil {
		curr.Next = head2
	}

	return mergedList
}

func mergesort(head *ListNode, length int) *ListNode {
	/*
			mergesort(list, len)
		- if list len == 1: return
		- else:
			- walk to midway of first half of list
			- call mergesort(node, len/2) on second half
			- set next of last node in first half to nil
			- call mergesort(list, len/2) on first half (original list reference)
			 - merge() first half and second half, return merged
	*/
	if length == 1 {
		return head
	}

	var leftLength, rightLength int
	if length%2 != 0 {
		leftLength = length / 2
		rightLength = leftLength + 1
	} else {
		leftLength = length / 2
		rightLength = length / 2
	}

	// Walk to midpoint
	curr := head
	for i := 1; i < length/2; i++ {
		curr = curr.Next
	}
	mid := curr.Next
	curr.Next = nil

	// Recursively merge sublists
	left := mergesort(head, leftLength)
	right := mergesort(mid, rightLength)

	return merge(left, right)
}

func sortList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	return mergesort(head, Len(head))
}

func main() {
	ll := createLL(0, false)
	Walk(ll)
	ll = sortList(ll)
	Walk(ll)

}
