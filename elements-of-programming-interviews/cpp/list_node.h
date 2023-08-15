
#pragma once

#include <iostream>
#include <memory>

#include "test_framework/fmt_print.h"
#include "test_framework/serialization_traits.h"

using std::make_shared;
using std::shared_ptr;

template <typename T>
struct ListNode {
  T data;

  // We need to use a shared pointer since multiple nodes may point to a
  // single node. For example, in the following list, two nodes, 1 and 4,
  // point to node 2.
  // 0->1->2->3->4
  //       ^     |
  //       |_____|
  shared_ptr<ListNode<T>> next;

  ListNode(T data = {}, shared_ptr<ListNode<T>> next = nullptr)
      : data(data), next(next) {}

  ~ListNode() {
    // Extra-long lists cause stack overflow with default destructor
    // implementation
    while (next && (next.use_count() == 1)) {
      auto next_next = next->next;
      next->next.reset();
      next = next_next;
    }
  }

  bool operator==(const ListNode<T>& that) const {
    const ListNode<T>* a = this;
    const ListNode<T>* b = &that;
    while (a && b) {
      if (a->data != b->data) {
        return false;
      }
      a = a->next.get();
      b = b->next.get();
    }
    return a == nullptr && b == nullptr;
  }
};

template <typename T>
bool EqualList(shared_ptr<ListNode<T>> a, shared_ptr<ListNode<T>> b) {
  return (!a && !b) || (a && b && *a == *b);
}

template <typename T>
std::shared_ptr<ListNode<T>> ConvertArrayToLinkedList(const std::vector<T>& v) {
  std::shared_ptr<ListNode<T>> head;
  for (auto it = rbegin(v); it != rend(v); ++it) {
    head = std::make_shared<ListNode<T>>(*it, head);
  }
  return head;
}

template <typename T>
std::ostream& operator<<(std::ostream& out, shared_ptr<ListNode<T>> node) {
  std::set<shared_ptr<ListNode<T>>> visited;
  bool first = true;

  while (node) {
    if (first) {
      first = false;
    } else {
      out << " -> ";
    }

    if (visited.count(node)) {
      if (node->next != node) {
        PrintTo(out, node->data);
        out << " -> ... -> ";
      }
      PrintTo(out, node->data);
      out << " -> ...";
      break;
    } else {
      PrintTo(out, node->data);
      visited.emplace(node);
    }
    node = node->next;
  }

  return out;
}

namespace JoshuaListTools {

shared_ptr<ListNode<int>> ReverseList(shared_ptr<ListNode<int>> head) {
  if (!head || !head->next) {
    return head;
  }
  shared_ptr<ListNode<int>> curr = head, next = head->next,
                            nextNext = head->next->next;
  head->next = nullptr;
  while (next) {
    nextNext = next->next;
    next->next = curr;
    curr = next;
    next = nextNext;
  }
  return curr;
}

shared_ptr<ListNode<int>> ConstructList(const int length) {
  if (!length) {
    return nullptr;
  }
  shared_ptr<ListNode<int>> head = make_shared<ListNode<int>>(0);
  shared_ptr<ListNode<int>> curr = head;
  for (int i = 0 + 1; i <= length; i++) {
    curr->next = make_shared<ListNode<int>>(i);
    curr = curr->next;
  }
  return head;
}

void PrintList(shared_ptr<ListNode<int>> head) {
  int i = 0;
  while (head) {
    printf("node %d: %d\n", i, head->data);
    head = head->next;
    i++;
  }
  printf("\n");
}

int MeasureListLength(shared_ptr<ListNode<int>> head) {
  int i = 0;
  while (head) {
    head = head->next;
    i++;
  }
  return i;
}
}  // namespace JoshuaListTools

template <typename T>
int ListSize(shared_ptr<ListNode<T>> node) {
  std::set<shared_ptr<ListNode<T>>> visited;
  int result = 0;

  while (node && !visited.count(node)) {
    ++result;
    visited.emplace(node);
    node = node->next;
  }
  return result;
}

namespace test_framework {
template <typename T>
struct SerializationTrait<shared_ptr<ListNode<T>>> {
  using serialization_type =
      shared_ptr<ListNode<typename SerializationTrait<T>::serialization_type>>;
  static const char* Name() {
    static std::string s =
        FmtStr("linked_list({})", SerializationTrait<T>::Name());
    return s.c_str();
  }

  static serialization_type Parse(const json& json_object) {
    auto v = SerializationTrait<std::vector<T>>::Parse(json_object);
    return ConvertArrayToLinkedList(v);
  }

  static std::vector<std::string> GetMetricNames(const std::string& arg_name) {
    return {FmtStr("size({})", arg_name)};
  }

  static std::vector<int> GetMetrics(const serialization_type& x) {
    return {static_cast<int>(ListSize(x))};
  }

  static bool Equal(const serialization_type& a, const serialization_type& b) {
    return EqualList(a, b);
  }
};

}  // namespace test_framework
