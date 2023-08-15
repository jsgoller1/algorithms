#include <stdexcept>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/serialization_traits.h"
#include "test_framework/test_failure.h"
using std::length_error;
using std::vector;

/*
  We can implement this with two stacks; whenever we push a new value in, if
  it's greater than the max's top, push that. If we pop the max's top, pop max
  too.
*/

class Stack {
 public:
  bool Empty() const { return vals.empty(); }
  int Max() const { return *(maxVals.end() - 1); }
  int Pop() {
    // NOTE: irl, throw exception for pop from empty stack.
    int val = *(vals.end() - 1);
    vals.pop_back();
    if (!maxVals.empty() && val == *(maxVals.end() - 1)) {
      maxVals.pop_back();
    }
    return val;
  }
  void Push(int x) {
    vals.push_back(x);
    if (maxVals.empty() || x >= *(maxVals.end() - 1)) {
      maxVals.push_back(x);
    }
    return;
  }

 private:
  vector<int> vals = vector<int>();
  vector<int> maxVals = vector<int>();
};
struct StackOp {
  std::string op;
  int argument;
};

namespace test_framework {
template <>
struct SerializationTrait<StackOp> : UserSerTrait<StackOp, std::string, int> {};
}  // namespace test_framework

void StackTester(const std::vector<StackOp>& ops) {
  try {
    Stack s;
    for (auto& x : ops) {
      if (x.op == "Stack") {
        continue;
      } else if (x.op == "push") {
        s.Push(x.argument);
      } else if (x.op == "pop") {
        int result = s.Pop();
        if (result != x.argument) {
          throw TestFailure("Pop: expected " + std::to_string(x.argument) +
                            ", got " + std::to_string(result));
        }
      } else if (x.op == "max") {
        int result = s.Max();
        if (result != x.argument) {
          throw TestFailure("Max: expected " + std::to_string(x.argument) +
                            ", got " + std::to_string(result));
        }
      } else if (x.op == "empty") {
        int result = s.Empty();
        if (result != x.argument) {
          throw TestFailure("Empty: expected " + std::to_string(x.argument) +
                            ", got " + std::to_string(result));
        }
      } else {
        throw std::runtime_error("Unsupported stack operation: " + x.op);
      }
    }
  } catch (length_error&) {
    throw TestFailure("Unexpected length_error exception");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"ops"};
  return GenericTestMain(args, "stack_with_max.cc", "stack_with_max.tsv",
                         &StackTester, DefaultComparator{}, param_names);
}
