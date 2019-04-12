/*
You are given two non-empty linked lists representing two nonnegative
integers. The digits are stored in reverse order and each of their nodes
contains a single digit. Add the two numbers and return the result
as a linked list. You may assume the two numbers do not contain any
leading zeros, except for the number zero itself.

Example:
In: (2->4->3) + (5->6->4)
Out: 7->0->8
Explanation: 342 + 465 = 807

Constraints:
  - Zero or positive numbers
-------------------------------------
In: two linked list heads
Out: int

- maintain two strings
- go node by node casting/appending to string
- reverse strings
- return atoi(str1) + atoi(str2)

The intended solution for this is probably to do something like keeping
track of the ones/tens/zeros place. Would that be simpler?

sum = 0
place = 1;
while node != nullptr:
  sum += node.val * place
  place *= 10

then do division for the opposite

IRL, we'd want to write a LL class (or use STL if one's available)
that does RAII cleanup, but not for leetcode (don't even care about
freeing stuff for this)
---------------------------------
*/

#include <iostream>

// Don't do this IRL
using namespace std;

// Definition for singly-linked list.
#pragma clang diagnostic ignored "-Wpadded"
struct ListNode {
  int val;
  ListNode* next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
 public:
  ListNode* intToList(int val) {
    ListNode empty{0};
    ListNode *head = &empty, *curr = &empty;

    // calculation is int((value / 10^place) % 10)
    while (val > 0) {
      curr->next = new ListNode{val % 10};
      curr = curr->next;
      val /= 10;
    }

    return head->next;
  }

  int listToInt(ListNode* node) {
    int sum = 0;
    int place = 1;
    while (node != nullptr) {
      sum += (node->val * place);
      place *= 10;
      node = node->next;
    }
    return sum;
  }

  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int val1 = listToInt(l1);
    // cout << val1 << endl;
    int val2 = listToInt(l2);
    // cout << val2 << endl;

    return intToList(val1 + val2);
  }
};

int main() {
  Solution s;
  ListNode lista1{0}, lista2{0}, lista3{9};
  lista1.next = &lista2;
  lista2.next = &lista3;

  ListNode listb1{0}, listb2{0}, listb3{1};
  listb1.next = &listb2;
  listb2.next = &listb3;

  ListNode* solution = s.addTwoNumbers(&lista1, &listb1);

  ListNode* oldptr;
  while (solution != nullptr) {
    cout << solution->val << endl;

    oldptr = solution;
    solution = solution->next;
    delete oldptr;
  }

  // cout << endl;
  return 0;
}
