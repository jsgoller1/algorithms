#include <memory>

#include "list_node.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::shared_ptr;

/* 
  If two singly linked lists share any node, they will have the same 
  final node, so we can traverse to the end and compare. The worst case
  is that two lists share only their final node, which we cannot determine
  without walking them completely so our best case is O(N) and O(c) space. 
  -----
  The book doesn't specify this, but the tests want the _first_ shared node, not 
  any shared node. We could find this in O(N^2) time and O(C) space by testing
  every node in l0 against every node in l1 (i.e. advance l0 one at a time and
  walk l1 each time). We could do it in O(N) time and space by adding every
  address of l1 to a set, and then checking each address of l0 against it,
  returning the first or nullptr. 
*/

#include <set>
using std::set;

shared_ptr<ListNode<int>> OverlappingNoCycleLists(
    shared_ptr<ListNode<int>> l0, shared_ptr<ListNode<int>> l1) {
      set<shared_ptr<ListNode<int>>>* l0_nodes = new set<shared_ptr<ListNode<int>>>();
      while(l0 != nullptr) {
        l0_nodes->insert(l0);
        l0 = l0->next;
      }
      
      shared_ptr<ListNode<int>> retval = nullptr;
      while(l1 != nullptr) {
        if (l0_nodes->find(l1) != l0_nodes->end()){
          retval = l1;
          break;
        }
        l1 = l1->next;
      }
      delete l0_nodes;
  return retval;
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
    throw TestFailure("Invalid result");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "l0", "l1", "common"};
  return GenericTestMain(
      args, "do_terminated_lists_overlap.cc", "do_terminated_lists_overlap.tsv",
      &OverlappingNoCycleListsWrapper, DefaultComparator{}, param_names);
}
