#include "list_node.h"
#include "test_framework/generic_test.h"

/*
0    1    2    3    4    5    6
A -> B -> C -> D -> E -> F -> G

ReverseSublist(2, 5)

0    1    2    3    4    5    6
A -> B -> F -> E -> D -> C -> G

- Have two pointers, to 5 (end, final) and 2 (start).
while (start != final)
- Set 2->next to 5->next
  - (start->next = end->next; end = start, start = start->next)
- Then set 3->next to 2
- Then set 4->next to 3
- Then set 5->next to 4

Alternative:
- Use subroutine to reverse sublist as full list
  - go through list two at a time, flipping
  - Return new head
- Do fixups sublist if needed.
- If head and end are the first and last nodes of the sublist:
  - if head != 1, we need to make head-1 point at new head
  - if end != list length, we need to make the new end point at old end's next.
*/

#define FIRST_NODE 1

shared_ptr<ListNode<int>> ConstructList(const int length) {
  if (!length) {
    return nullptr;
  }
  shared_ptr<ListNode<int>> head = make_shared<ListNode<int>>(FIRST_NODE);
  shared_ptr<ListNode<int>> curr = head;
  for (int i = FIRST_NODE + 1; i <= length; i++) {
    curr->next = make_shared<ListNode<int>>(i);
    curr = curr->next;
  }
  return head;
}

void PrintList(shared_ptr<ListNode<int>> head) {
  int i = FIRST_NODE;
  while (head) {
    printf("node %d: %d\n", i, head->data);
    head = head->next;
    i++;
  }
  printf("\n");
}

shared_ptr<ListNode<int>> ReverseList(shared_ptr<ListNode<int>> head,
                                      shared_ptr<ListNode<int>> end = nullptr) {
  if (!head) {
    return head;
  }
  shared_ptr<ListNode<int>> curr = head, next = head->next, newNext = nullptr;
  curr->next = (end) ? end->next : nullptr;
  while (next && curr != end) {
    newNext = next->next;
    next->next = curr;
    curr = next;
    next = newNext;
  }

  return curr;
}

shared_ptr<ListNode<int>> ReverseSublist(shared_ptr<ListNode<int>> L, int head,
                                         int end) {
  // If head is 0, use ReverseList() as is. If not, need to do fixup.
  // Don't need to worry about end; ReverseList handles it.
  if (!L) {
    return nullptr;
  }
  shared_ptr<ListNode<int>> preHeadP = nullptr, headP = nullptr, endP = nullptr,
                            curr = L;
  for (int i = FIRST_NODE; curr != nullptr; i++, curr = curr->next) {
    if (i == head - 1) {
      preHeadP = curr;
    }
    if (i == head) {
      headP = curr;
    }
    if (i == end) {
      endP = curr;
    }
  }

  // printf("\nReversing sublist. Start: %d, End: %d\n", headP ? headP->data :
  // -1,   endP ? endP->data : -1);
  shared_ptr<ListNode<int>> newHead = ReverseList(headP, endP);
  if (head == FIRST_NODE) {
    L = newHead;
  } else if (preHeadP) {
    preHeadP->next = newHead;
  }
  return L;
}

int main(int argc, char* argv[]) {
  /*
  auto head = ConstructList(2);
  PrintList(head);
  head = ReverseSublist(head, 13, 14);
  PrintList(head);
  */

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L", "start", "finish"};
  return GenericTestMain(args, "reverse_sublist.cc", "reverse_sublist.tsv",
                         &ReverseSublist, DefaultComparator{}, param_names);
}
