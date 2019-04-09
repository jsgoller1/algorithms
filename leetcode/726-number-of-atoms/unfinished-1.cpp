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

- Each parenthesized part of the formula can be counted with a hashmap
of molecules to numbers
- Each time we encounter an open paren, we start a new "context",
count molecules til we see a close paren, and then merge with the old context
- Once the whole string is parsed, we convert the hashmap to a string and return

- The hard part of this is correctly dividing the formula into tokens:
  - Single character atom
  - Two character atom
  - Number
  - Open or close paren

- C++ doesn't support multiple returns, so writing a getNextToken() or recursive
parse() function will be difficult because it will need to return both the
context it parsed and the index the caller needs to continue from.

- If we use a stack of hashmaps, we don't need to recurse; we just push the
old context onto the stack and start a new one.

- How to parse the string character by character:
  - If we get an uppercase character, we need to look at the next character.
    - If it's a number, we get the full number
    - If it's a lowercase letter. concat with first letter and repeat
    - If it's a paren or uppercase letter, back out, treat count as 1, and add
      to hashmap
  - If we get an open paren, push old context / recurse to new context
  - If we get a close paren, look one past it for number to see if we need
    to multiply our current context and multiply if so, then combine and
    return it / pop it.

*/

#include <iostream>
#include <map>
#include <string>

// Don't do this
using namespace std;

class Solution {
 public:
  string countOfAtoms(string formula) {
    /*
    create stack of hashmaps of strings to ints
    start at index 0
    while index < len(string):
      if string[index] is upper case:
        symbol = string[index]
        count = string{}
        if string[next] is lowercase:
          symbol += string[next]
          look at following character
        if next is number:
          get full number, then add uppercase: number to hashmap
        else (uppercase or paren):
          add string[index]: 1 to hashmap

      else if open paren:
        // push context onto stack, start new context
      else if close paren:
        // look one past, get number if it's there and multiple with
        // context, then combine with previous context
    pop last context off stack, convert into string, return

    */
  }
};

int main() {
  Solution s;
  cout << (s.countOfAtoms("HeS3O") == string{"HeS3O"}) << endl;
  cout << (s.countOfAtoms("H2(SO4)3") == string{"H2S3O12"}) << endl;
  cout << (s.countOfAtoms("H23") == string{"H23"}) << endl;
  cout << (s.countOfAtoms("") == string{""}) << endl;
  cout << (s.countOfAtoms("H(O(S2)3)2") == string{"HO6S12"}) << endl;
}
