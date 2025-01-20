#include <string>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::pair;
using std::string;
using std::vector;

/*
- Create an array of indexes and lengths, one for each word.
- Reverse the array
- Copy into a new string, then overwrite old
- Time: O(n): each step (array creation, reversal, copying, overwriting) is
linear
- Takes n space for array of pairs, and n extra space for new string

- Happy cases:
  "bob talks to alice" -> "alice to talks bob"
- Edge cases:
  - Empty string
  - String contains one word ("aaaaaaa")
  - Assuming words are delimited by whitespaces; don't actually know
  - What if there are multiple whitespaces between words? Assume not a case.

 Then just reverse this list and copy it into a string.
 -----
 Better: mark where words are in the string. Reverse the string, then reverse
each word.
*/

vector<int> markSpaces(const string& s) {
  vector<int> spaceIdx;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == ' ') {
      spaceIdx.push_back(i);
    }
  }
  spaceIdx.push_back(s.size());
  return spaceIdx;
}

void ReverseWords(string* s) {
  string& sentence = *s;
  reverse(sentence.begin(), sentence.end());
  vector<int> spaces = markSpaces(sentence);
  int left = 0;
  for (int i = 0; i < spaces.size(); i++) {
    int right = spaces[i];
    reverse(sentence.begin() + left, sentence.begin() + right);
    left = spaces[i] + 1;
  }
}

string ReverseWordsWrapper(TimedExecutor& executor, string s) {
  string s_copy = s;

  executor.Run([&] { ReverseWords(&s_copy); });

  return s_copy;
}

int main(int argc, char* argv[]) {
  /**/
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "s"};
  return GenericTestMain(args, "reverse_words.cc", "reverse_words.tsv",
                         &ReverseWordsWrapper, DefaultComparator{},
                         param_names);
}
