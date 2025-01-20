#include <memory>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using JoshuaListTools::PrintList;
using std::shared_ptr;

/*

Approach 1 (not implemented). O(n) time, O(c) space, but modifies list.
- Measure length of both
- Reverse both twice
- Remeasure lengths:
  - If lengths change, they overlap (one of them will be shorter because
    reversal will break joint)
- Walk both from heads; when shorter's next is null, set it to other's next.
  Then return that next.

Insight: If two lists are the same length and overlap, then they both meet at
their ith node (the shared portion will be the same length for both, so they can
only have the same overall length if their unshared portions are equally as
long).

Approach 2 (implemented). O(n) time, O(c) space, no side effects.
We only need to tell if two lists overlap, and if so we can return any node
in them. They're both sure to terminate, so why not just iterate to the end
of both and compare the address of the final nodes?

Unfortunately the book doesn't say this, but the test cases expect you to
return the first node they have in common, not any of them.


Approach 3 (implemented). O(n) time, O(c) space, no side effects.
- Measure length of both
- If lengths are unequal, advance the head of the longer one until they are.
- Advance heads one at a time until a joint node is found (or end is reached)
*/

shared_ptr<ListNode<int>> OverlappingNoCycleListsAnyNode(
    shared_ptr<ListNode<int>> l0, shared_ptr<ListNode<int>> l1) {
  if (!l0 || !l1) {
    return nullptr;
  }
  PrintList(l0);
  PrintList(l1);

  while (l0->next != nullptr) {
    l0 = l0->next;
  };
  while (l1->next != nullptr) {
    l1 = l1->next;
  };

  return (l0.get() == l1.get()) ? l0 : nullptr;
}

shared_ptr<ListNode<int>> OverlappingNoCycleLists(
    shared_ptr<ListNode<int>> l0, shared_ptr<ListNode<int>> l1) {
  if (!l0 || !l1) {
    return nullptr;
  }
  int l0Length = JoshuaListTools::MeasureListLength(l0),
      l1Length = JoshuaListTools::MeasureListLength(l1);
  while (l0Length > l1Length) {
    l0 = l0->next;
    l0Length--;
  }
  while (l1Length > l0Length) {
    l1 = l1->next;
    l1Length--;
  }

  while (l0 && l1) {
    if (l0 == l1) {
      return l0;
    }
    l0 = l0->next;
    l1 = l1->next;
  }
  return nullptr;
}

void OverlappingNoCycleListsWrapper(TimedExecutor& executor,
                                    shared_ptr<ListNode<int>> l0,
                                    shared_ptr<ListNode<int>> l1,
                                    shared_ptr<ListNode<int>> common) {
  if (common) {
    if (l0) {
      auto i = l0;
      while (i->next) {
        i = i->next;
      }
      i->next = common;
    } else {
      l0 = common;
    }

    if (l1) {
      auto i = l1;
      while (i->next) {
        i = i->next;
      }
      i->next = common;
    } else {
      l1 = common;
    }
  }

  auto result = executor.Run([&] { return OverlappingNoCycleLists(l0, l1); });

  if (result != common) {
    printf("Invalid result; expected: %p (%d), got %p (%d)\n", common.get(),
           common->data, result.get(), result->data);
    throw TestFailure("Test failed.\n");
  }
}

int main(int argc, char* argv[]) {
  /*
  shared_ptr<ListNode<int>> head = ConstructList(5);
  PrintList(head);
  auto newHead = ReverseList(head);
  PrintList(newHead);
  */

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0", "l1", "common"};
  return GenericTestMain(
      args, "do_terminated_lists_overlap.cc", "do_terminated_lists_overlap.tsv",
      &OverlappingNoCycleListsWrapper, DefaultComparator{}, param_names);
}
