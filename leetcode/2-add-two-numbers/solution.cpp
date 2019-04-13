// See alternate for full SUPER writeup

/*
- a function that takes the two list heads
- adds each one, stores result % 10 in new node; adds carry if set, sets carry
if need be
- if either head is null, just add value of other head
- proceed til both heads are null
----------------------------------------------------------
Runtime: 28 ms, faster than 98.15% of C++ online submissions for Add Two
Numbers.

Memory Usage: 10.3 MB, less than 99.76% of C++ online submissions for
Add Two Numbers.

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
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode empty{0};
    ListNode *head = &empty, *curr = &empty;
    bool carry = false;
    int total = 0;

    // calculation is long((value / 10^place) % 10)
    while (l1 != nullptr || l2 != nullptr) {
      curr->next = new ListNode{0};
      curr = curr->next;
      if (l1 == nullptr) {
        total = l2->val;
        l2 = l2->next;
      } else if (l2 == nullptr) {
        total = l1->val;
        l1 = l1->next;
      } else {
        total = l1->val + l2->val;
        l1 = l1->next;
        l2 = l2->next;
      }
      total += (carry ? 1 : 0);
      carry = (total >= 10 ? true : false);
      curr->val = total % 10;
    }

    // in the event the two largest places cause carry, add a node
    curr->next = (carry ? new ListNode{1} : nullptr);

    return head->next;
  }
};

int main() {
  Solution s;
  ListNode lista1{9}, lista2{8}, lista3{9};
  lista1.next = &lista2;
  // lista2.next = &lista3;

  ListNode listb1{1}, listb2{0}, listb3{1};
  // listb1.next = &listb2;
  // listb2.next = &listb3;

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
