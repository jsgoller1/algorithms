#include <set>
#include <stdexcept>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"

/*
- We can do (floyd test) tortise-and-hare method to determine if a list contains
a cycle.
- Overlapping cyclic lists are not ensured to join cycle at the same node, but
  eventually both cross over the same node.

Cases:
- Either is null
- One has cycle and other doesn't (no overlap)
- No overlap, no cycles
- No overlap, both have cycles
- Overlap, no cycle
- Overlap and cycle
  - Both lists are same list (special overlap case)

Null test
First test for cycles/length; both must agree.
  - Neither contains cycles: reuse previous overlap test (shorten and compare)
    or just return last node
  - Both contain cycles: can get first node of cycle for each, and then rotate
    around cycle until either is found
*/

int ListLength(shared_ptr<ListNode<int>> head) {
  int length = 0;
  shared_ptr<ListNode<int>> slow = head, fast = head;
  while (slow) {
    slow = slow->next;
    length++;
    fast = (fast) ? fast->next : fast;
    fast = (fast) ? fast->next : fast;
    if (slow && slow == fast) {
      // printf("%p == %p\n", slow.get(), fast.get());
      return -1;
    }
  }
  return length;
}

shared_ptr<ListNode<int>> GetFirstCycleNode(shared_ptr<ListNode<int>> head) {
  // NOTE: breaks if used on an acyclic list.
  if (!head) {
    return nullptr;
  }
  shared_ptr<ListNode<int>> slow = head, fast = head;
  do {
    slow = slow->next;
    fast = fast->next->next;
  } while (slow != fast);
  slow = head;
  while (slow != fast) {
    slow = slow->next;
    fast = fast->next;
  }
  return fast;
}

shared_ptr<ListNode<int>> CyclicOverlapTest(shared_ptr<ListNode<int>> l0,
                                            shared_ptr<ListNode<int>> l1) {
  if (!l0 || !l1) {
    return nullptr;
  }
  // NOTE: breaks if used on an acyclic list.
  l0 = GetFirstCycleNode(l0);
  shared_ptr<ListNode<int>> l0Origin = l0;
  l1 = GetFirstCycleNode(l1);

  while (l0 != l1) {
    l0 = l0->next;
    if (l0 == l0Origin) {
      return nullptr;
    }
  }
  return l0;
}

shared_ptr<ListNode<int>> AcyclicOverlapTest(shared_ptr<ListNode<int>> l0,
                                             shared_ptr<ListNode<int>> l1) {
  // NOTE: breaks if used on a cyclic list.

  if (!l0 || !l1) {
    return nullptr;
  }
  while (l0->next) {
    l0 = l0->next;
  }
  while (l1->next) {
    l1 = l1->next;
  }
  return (l0 == l1) ? l0 : nullptr;
}

shared_ptr<ListNode<int>> OverlappingLists(shared_ptr<ListNode<int>> l0,
                                           shared_ptr<ListNode<int>> l1) {
  if (!l0 || !l1) {
    return nullptr;
  }
  int l0Size = ListLength(l0), l1Size = ListLength(l1);
  if ((l0Size == -1 || l1Size == -1) && (l0Size != l1Size)) {
    return nullptr;
  }
  if (l0Size == -1) {
    return CyclicOverlapTest(l0, l1);

  } else {
    return AcyclicOverlapTest(l0, l1);
  }
}

/*-----------*/

void OverlappingListsWrapper(TimedExecutor& executor,
                             shared_ptr<ListNode<int>> l0,
                             shared_ptr<ListNode<int>> l1,
                             shared_ptr<ListNode<int>> common, int cycle0,
                             int cycle1) {
  if (common) {
    if (!l0) {
      l0 = common;
    } else {
      auto it = l0;
      while (it->next) {
        it = it->next;
      }
      it->next = common;
    }

    if (!l1) {
      l1 = common;
    } else {
      auto it = l1;
      while (it->next) {
        it = it->next;
      }
      it->next = common;
    }
  }

  if (cycle0 != -1 && l0) {
    auto last = l0;
    while (last->next) {
      last = last->next;
    }
    auto it = l0;
    while (cycle0-- > 0) {
      if (!it) {
        throw std::runtime_error("Invalid input data");
      }
      it = it->next;
    }
    last->next = it;
  }

  if (cycle1 != -1 && l1) {
    auto last = l1;
    while (last->next) {
      last = last->next;
    }
    auto it = l1;
    while (cycle1-- > 0) {
      if (!it) {
        throw std::runtime_error("Invalid input data");
      }
      it = it->next;
    }
    last->next = it;
  }

  std::set<shared_ptr<ListNode<int>>> common_nodes;
  auto it = common;
  while (it && common_nodes.count(it) == 0) {
    common_nodes.insert(it);
    it = it->next;
  }

  auto result = executor.Run([&] { return OverlappingLists(l0, l1); });

  if (!((common_nodes.empty() && result == nullptr) ||
        common_nodes.count(result) > 0)) {
    throw TestFailure("Invalid result");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0",     "l1",
                                       "common",   "cycle0", "cycle1"};
  return GenericTestMain(args, "do_lists_overlap.cc", "do_lists_overlap.tsv",
                         &OverlappingListsWrapper, DefaultComparator{},
                         param_names);
}
