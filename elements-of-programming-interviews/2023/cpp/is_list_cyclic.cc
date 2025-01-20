#include <memory>
#include <set>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::set;
using std::shared_ptr;

// Normal way: tortise and hare method; list must be finite. But this doesn't
// return the first node of the cycle.

// O(n) space - just use a set.

// O(c) space, O(n^2) time; use Floyd's method (tortise/hare) to find cycle.
// Then, start another pointer (turtle; moves one at a time) off from the start
// of the list. Each time turtle moves, have the tortise pointer do a full lap
// until it reaches either the hare or the turtle. If tortise reaches hare,
// turtle is not on cycle yet. If tortise reaches turtle, turtle has reached
// first node of cycle.

shared_ptr<ListNode<int>> HasCycleLinearSpace(
    const shared_ptr<ListNode<int>>& head) {
  shared_ptr<ListNode<int>> curr = head;
  set<shared_ptr<ListNode<int>>> visited;
  while (curr && visited.find(curr) == visited.end()) {
    visited.insert(curr);
    curr = curr->next;
  }
  return curr;
}

/*
  - Suppose we use the Tortise/Hare strategy to force the two pointers ("slow"
  and "fast") to meet.
  - Assume this list:
              _______________
              V              |
    0 -> 1 -> 2 -> 3 -> 4 -> 5

  - The linked list can be described using the following:
    - A: Nodes not in cycles (2: 0, and 1)
    - B: Distance from start of cycle meeting point (2)
        - (0,0), (1,2), (2,4), (3, 2), (4,4)
    - C: cycle length (4: 2,3,4,5)
  - When slow meets fast, slow traveled through all of the non-cycle nodes (A)
  and the distance from the first cycle node to the meeting point to B, so
  A+B.
  - Because fast moves 2 nodes for each of slow's 1, fast has moved 2(A+B)
  when they meet; the extra A+B that fast has moved before meeting slow happens
  inside the loop.
  - Suppose we now reset slow; fast is still at the meeting point:
    - Slow is now A away from the first node in the cycle
    - Fast is C-B away from the first node in the cycle.
    - If A = C-B, then they meet at the first node of the cycle.
      - When hare traveled the first A+B, it arrived at the meeting point.
        When it then traveled another A+B, it arrived at the meeting point
        again. This does _not_ mean that C = A+B, but it does mean that C*N =
  A+B.
      - If N = 1 (so C = A+B), then when both nodes travel A forward, they will
  meet at the first node of the cycle.
      - If N > 1, then C < A+B, so hare completes several cycles as tortise
  moves A. However, after some number of cycles, tortise will be C away from the
  meeting point, and hare will be at the meeting point. Hare moves forward C-B
  to get to the first cycle point. Turtle will also move forward C-B along the
  non-cycle points, arriving simultaneously at the first cycle point.


*/

shared_ptr<ListNode<int>> HasCycle(const shared_ptr<ListNode<int>>& head) {
  shared_ptr<ListNode<int>> slow = head, fast = head;
  do {
    if (!slow || !fast || !fast->next) {
      // no cycle
      return nullptr;
    }

    slow = slow->next;
    fast = fast->next->next;
  } while (fast != slow);

  slow = head;
  while (fast != slow) {
    fast = fast->next;
    slow = slow->next;
  }
  return fast;
}

void HasCycleWrapper(TimedExecutor& executor,
                     const shared_ptr<ListNode<int>>& head, int cycle_idx) {
  int cycle_length = 0;
  if (cycle_idx != -1) {
    if (!head) {
      throw std::runtime_error("Can't cycle empty list");
    }
    shared_ptr<ListNode<int>> cycle_start, cursor = head;
    while (cursor->next) {
      if (cursor->data == cycle_idx) {
        cycle_start = cursor;
      }
      cursor = cursor->next;
      cycle_length += !!cycle_start;
    }
    if (cursor->data == cycle_idx) {
      cycle_start = cursor;
    }
    if (!cycle_start) {
      throw std::runtime_error("Can't find a cycle start");
    }
    cursor->next = cycle_start;
    cycle_length++;
  }
  shared_ptr<ListNode<int>> result =
      executor.Run([&] { return HasCycle(head); });

  if (cycle_idx == -1) {
    if (result != nullptr) {
      throw TestFailure("Found a non-existing cycle");
    }
  } else {
    if (result == nullptr) {
      throw TestFailure("Existing cycle was not found");
    }

    auto cursor = result;
    do {
      cursor = cursor->next;
      cycle_length--;
      if (!cursor || cycle_length < 0) {
        throw TestFailure(
            "Returned node does not belong to the cycle or is not the "
            "closest node to the head");
      }
    } while (cursor != result);

    if (cycle_length != 0) {
      throw TestFailure(
          "Returned node does not belong to the cycle or is not the closest "
          "node to the head");
    }
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "head", "cycle_idx"};
  return GenericTestMain(args, "is_list_cyclic.cc", "is_list_cyclic.tsv",
                         &HasCycleWrapper, DefaultComparator{}, param_names);
}
