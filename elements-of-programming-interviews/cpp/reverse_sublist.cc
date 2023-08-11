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


*/

shared_ptr<ListNode<int>> ReverseSublist(shared_ptr<ListNode<int>> L, int start,
                                         int finish) {
  // TODO - you fill in here.
  return L;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"L", "start", "finish"};
  return GenericTestMain(args, "reverse_sublist.cc", "reverse_sublist.tsv",
                         &ReverseSublist, DefaultComparator{}, param_names);
}
