#include "list_node.h"
#include "test_framework/generic_test.h"

/*
  - keep place, iterate through, (digit + digit) * place
  - need carry if adding node by node.
  - negatives? can handle by reading both to ints first then adding
  - no empty list
*/

shared_ptr<ListNode<int>> AddTwoNumbers(shared_ptr<ListNode<int>> L1,
                                        shared_ptr<ListNode<int>> L2) {
  int carry = 0;
  int total = 0;
  shared_ptr<ListNode<int>> current = make_shared<ListNode<int>>();
  shared_ptr<ListNode<int>> head = current;
  while (L1 || L2 || carry) {
    int val1 = (L1 != nullptr) ? L1->data : 0;
    int val2 = (L2 != nullptr) ? L2->data : 0;
    L1 = (L1 == nullptr) ? nullptr : L1->next;
    L2 = (L2 == nullptr) ? nullptr : L2->next;

    // Assuming no negatives.
    total = (val1 + val2 + carry) % 10;
    carry = (val1 + val2 + carry >= 10) ? 1 : 0;

    current->next = make_shared<ListNode<int>>();
    current->next->data = total;
    current = current->next;
  }
  return head->next;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L1", "L2"};
  return GenericTestMain(args, "int_as_list_add.cc", "int_as_list_add.tsv",
                         &AddTwoNumbers, DefaultComparator{}, param_names);
}
