/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
------------------------------------------------
- Input can contain three different symbols or be empty
- Parse l-to-r and maintain three different stacks
  - push any opening symbols
  - pop the right stack when we see a closer
  - if we pop and empty stack, return false
  - if any stacks nonempty at the end, return false
- return true

- actually don't even need stacks; use ints
- actually do need to use stack; ({)} is invalid but will trick ints
------------------------------------
Runtime: 4 ms, faster than 100.00% of C++ online submissions for Valid
Parentheses.

Memory Usage: 8.5 MB, less than 99.75% of C++ online submissions
for Valid Parentheses.
*/

#include <iostream>
#include <stack>
#include <string>

using std::cout;
using std::endl;
using std::stack;
using std::string;

class Solution {
 public:
  bool isValid(string s) {
    stack<char> symbols;

    for (auto symbol : s) {
      switch (symbol) {
        case '{':
        case '(':
        case '[':
          symbols.push(symbol);
          break;
        case ']':
          if (symbols.empty() || (symbols.top() != '[')) {
            return false;
          } else {
            symbols.pop();
          }
          break;
        case ')':
          if (symbols.empty() || (symbols.top() != '(')) {
            return false;
          } else {
            symbols.pop();
          }
          break;
        case '}':
          if (symbols.empty() || (symbols.top() != '{')) {
            return false;
          } else {
            symbols.pop();
          }
          break;
      }
    }
    return symbols.empty();
  }
};

int main() {
  Solution s;
  cout << (s.isValid("()") == true) << endl;
  cout << (s.isValid("") == true) << endl;
  cout << (s.isValid("(({)))") == false) << endl;
  cout << (s.isValid("([)]") == false) << endl;
  cout << (s.isValid("()[]{}") == true) << endl;

  return 0;
}
