#include <stack>
#include <string>

#include "test_framework/generic_test.h"
using std::cout;
using std::endl;
using std::stack;
using std::string;

/*
Cases:
  - Empty string
  - String of the following, comma separated (valid/well formed)
    - Last item in string won't be followed by comma
    - Integers, possibly prefixed with -
    - A B (op) expression; op can be + / * -
      - Division should be integer division, rounded down

Examples:
- "-356" -> -356
- "2,3,*" -> 6
- "2,3,*,2,3,*,*" -> 36

Approach:
  - Helper function for converting num strings to ints (stoi?)
  - Helper for determining symbol or int
  - Once we have literal values, can just push to stack and pop/combine/repush
on operators

*/

void applyOperator(const string& expr, stack<int>& data) {
  int op2 = data.top();
  data.pop();
  int op1 = data.top();
  data.pop();

  int val;
  switch (expr[0]) {
    case '+':
      // printf("pushing %d\n", op1 + op2);
      data.push(op1 + op2);
      break;
    case '-':
      data.push(op1 - op2);
      break;
    case '*':
      data.push(op1 * op2);
      break;
    case '/':
      data.push(op1 / op2);
      break;
  }
}

bool isOperator(const string& expr) {
  return expr == "-" || expr == "+" || expr == "/" || expr == "*";
}

int Evaluate(const string& expression) {
  stack<int> data;
  auto start_it = expression.begin(), end_it = expression.begin();
  for (int i = 0; i <= expression.length(); i++) {
    if (expression[i] != ',' && i != expression.length()) {
      continue;
    }
    end_it = expression.begin() + i;
    string substr(start_it, end_it);
    if (!isOperator(substr)) {
      // cout << "i: " << i << endl;
      // cout << "pushing val: " << substr << endl;
      data.push(stoi(substr));
    } else {
      // cout << "Applying operator: " << substr << endl;
      applyOperator(substr, data);
    }
    start_it = end_it + 1;
  }

  return data.top();
}

int main(int argc, char* argv[]) {
  /*
printf("\n%d\n", Evaluate("3"));
printf("%d\n", Evaluate("-3"));
printf("%d\n", Evaluate("3,3,+"));
printf("%d\n", Evaluate("3,3,+,50,-2,*,+"));
*/

  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"expression"};
  return GenericTestMain(args, "evaluate_rpn.cc", "evaluate_rpn.tsv", &Evaluate,
                         DefaultComparator{}, param_names);
}
