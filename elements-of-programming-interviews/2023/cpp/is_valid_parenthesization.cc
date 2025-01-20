#include <stack>
#include <string>

#include "test_framework/generic_test.h"
using std::stack;
using std::string;

/*
- String can contain [], (), {}
- Invalid if:
  - pop from empty: "}"
  - unclosed: "()"
  - interleaved: "{(})"
Can we just use one stack and push all openers into it? Error if nonempty at
end, pop from empty, or pop doesn't match.
*/

bool isPushable(char c) { return c == '[' || c == '(' || c == '{'; }
bool isPoppable(char c) { return c == ']' || c == ')' || c == '}'; }
char getOpener(char c) {
  switch (c) {
    case ']':
      return '[';
    case ')':
      return '(';
    case '}':
      return '{';
    default:
      return '!';
  }
}

bool IsWellFormed(const string& s) {
  stack<char> parens;
  for (char c : s) {
    if (isPushable(c)) {
      parens.push(c);
    } else if (isPoppable(c)) {
      if (parens.empty() || parens.top() != getOpener(c)) {
        return false;
      } else {
        parens.pop();
      }
    }
  }
  return parens.empty();
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_valid_parenthesization.cc",
                         "is_valid_parenthesization.tsv", &IsWellFormed,
                         DefaultComparator{}, param_names);
}
