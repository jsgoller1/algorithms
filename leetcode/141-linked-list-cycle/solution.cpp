/*
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
-----------------------------------------------
In: ListNode head
Out: bool

- Every list is either cyclic or it terminates
- Tortise-and-the-hare method:
  - start two pointers at head of list
    - hare moves two places forward
    - tortise moves one place forward
    - if they are ever at the same node, a cycle exists
    - the hare will always hit the end first, so check if it's at the end and
quit if so.
- O(c) for space, and O(N) for time
-----------------------------------
Runtime: 12 ms, faster than 99.33% of C++ online submissions for Linked List
Cycle.

Memory Usage: 9.6 MB, less than 92.26% of C++ online submissions for Linked List
Cycle.
*/

#include <iostream>

using std::cout;
using std::endl;

#pragma clang diagnostic ignored "-Wpadded"
// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
 public:
  bool hasCycle(ListNode *head) {
    ListNode *fast = head;
    ListNode *slow = head;
    do {
      if (fast == nullptr || fast->next == nullptr ||
          fast->next->next == nullptr) {
        return false;
      } else {
        fast = fast->next->next;
        // slow will always trail behind fast, so it will never encounter
        // a nullptr that fast hasn't encountered already
        slow = slow->next;
      }
    } while (slow != fast);
    return true;
  }
};

int main() {
  Solution s;
  ListNode ll1(1), ll2(2), ll3(3), ll4(4);
  ll1.next = &ll2;
  ll2.next = &ll3;
  ll3.next = &ll4;
  cout << s.hasCycle(&ll1) << endl;
  ListNode ll5(5);
  ll4.next = &ll5;
  ll5.next = &ll1;
  cout << s.hasCycle(&ll1) << endl;
  cout << s.hasCycle(nullptr) << endl;
}
