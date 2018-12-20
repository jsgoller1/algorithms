"""
Given a chemical formula (given as a string), return the count of each atom. An atomic element
always starts with an uppercase character, then zero or more lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the count is greater than 1. If
the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its
count (if that count is more than 1), and so on.
---------------------------------------------------
I did this with @ozan during a mock interview. My initial approach was:
- maintain a symbol stack
- get each token (an atomic symbol, a number, or a paren) from the input formula
  - push the symbol onto the stack (casting "12" to literal 12 first) unless it's a closed paren
  - if it's a closed paren, get the number that follows and either append it to every symbol
    on the stack or multiply the existing symbol's count by it; then push everything back on the stack
- finally, read out the stack, obtain counts of symbols, and cast to the final string in sorted order.

Oz had a better idea:
- maintain hashtables like "frames"; start with an empty one and add atomic symbol counts as we parse tokens from the string
- if we encounter a paren, push the current hashtable and start a new one; get the counts til we hit the close paren
- multiply the number following the close paren by everything in our current frame, then merge with the previous frame.
- at the end, read out the keys of our "top level frame" in sorted order

I will implement oz's idea here.
"""
import collections


class Solution:
    def isInt(self, token):
        try:
            return type(int(token)) == int
        except ValueError:
            return False

    def getNextToken(self, formula, idx):
        if idx >= len(formula):
            return ""

        initialIdx = idx
        token = formula[idx]
        if token in ['(', ')']:
            return token
        elif str.isdigit(token):
            idx += 1
            while idx < len(formula) and str.isdigit(formula[idx]):
                token += formula[idx]
                idx += 1
        else:
            if idx < len(formula)-1 and str.islower(formula[idx+1]):
                token += formula[idx+1]
        return token

    def countOfAtoms(self, formula):
        idx = 0
        stack = []
        frame = collections.Counter()
        while idx < len(formula):
            token = self.getNextToken(formula, idx)
            idx += len(token)
            if token == '(':
                stack.append(frame)
                frame = collections.Counter()
            elif token == ')':
                # Get following counter if it exists, multiply
                # counts in existing frame, merge with
                # previous frame
                count = self.getNextToken(formula, idx)
                if count != "":
                    idx += len(count)
                    for key in frame:
                        frame[key] *= int(count)
                stack[-1] += frame
                frame = stack.pop()
            else:
                # We either got an atomic symbol or a number, and
                # numbers only come after symbols
                nextToken = self.getNextToken(formula, idx)
                if self.isInt(nextToken):
                    idx += len(nextToken)
                    frame[token] += int(nextToken)
                else:
                    frame[token] += 1

        solution = ""
        for key in sorted(frame.keys()):
            solution += key
            if frame[key] > 1:
                solution += str(frame[key])
        return solution


if __name__ == '__main__':
    s = Solution()
    assert s.countOfAtoms("") == ""
    assert s.countOfAtoms("H2O") == "H2O"
    assert s.countOfAtoms("Mg(OH)2") == "H2MgO2"
    assert s.countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4"
    assert s.countOfAtoms("H50") == "H50"
    assert s.countOfAtoms("(NB3)33") == "B99N33"
    assert s.countOfAtoms("F(NB3)33") == "B99FN33"
