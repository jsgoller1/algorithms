/*
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more
lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count
is greater than 1. If the count is 1, no digits will follow. For example, H2O
and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example,
H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a
formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following
form: the first name (in sorted order), followed by its count (if that count is
more than 1), followed by the second name (in sorted order), followed by its
count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Note:
- All atom names consist of lowercase letters, except for the first character
which is uppercase.
- The length of formula will be in the range [1, 1000].
- $formula will only consist of letters, digits, and round parentheses, and is a
valid formula as defined in the problem.
------------------------------------------------
in: string, molecular formula
out: string, same formula with no parens or repeated elements

- parse()
- To keep track of the overall count of each molecule, we need to maintain
a map of symbols to characters. This starts as empty, and at the end of the
function can be turned into a string
- The parsing logic should not modify the string, so it needs to keep
track of its position in the string
- Parens can be handled by recursing, creating a new local context,
parsing, then combining each symbol's count with the multiplier,
and returning / merging with the global context
- We can either keep references to the global context, or return it;
if we return it, we can't return the last index.
- Tokenizing is the tricky part:
  - A capital letter can be followed by:
    - Another capital, meaning the first one is one molecule
    - A lowercase letter, meaning both letters are one molecule
    - A number, indicating count
    - A paren


- After last parse, convert():
  - takes dict, returns string of symbols
*/

#include <iostream>
#include <map>
#include <string>

// Don't do this
using namespace std;

class Solution {
 public:
  /*
   map<string, int> mergeDicts(map<string, int> m1, map<string, int> m2) {}

   string dictToFormula(map<string, int> m) {}

   int parse(string formula, map<string, int> *globalCtx, int i) {
     // map<string, int> localCtx;
     return 0;
   }

   string countOfAtoms(string formula) {
     map<string, int> globalCtx;

     // Don't need returned index;
     parse(formula, &globalCtx, 0);
     return dictToFormula(globalCtx);
   }
   */
};

int main() {
  string str{"ABCD"};
  while (!str.empty()) {
    cout << str[str.size() - 1] << endl;
    str.pop_back();
  }
  return 0;
}
