// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

// #define endl "\n"  // std::endl causes a flush, adds unnecessary time

// --- Abbreviations --
#define rep(i, n) for (int i = 0; i < (n); i++)

/*
  - Keep vector of pairs <score, string>
  - Score each string, insert in vector O(n^2)
  - Sort, O(n*log(n))
  - Print in order

  score():
    Init zero
    For each letter, add 1 if letter to its right comes before it

  Option 1:
  Do N*2 comparisons, figure out how many letters after each are wrong;
  strings up to 50 so this could be 2500, with 100 possible strings is 250,000
  comparisons, not too many (comparison is a few nanoseconds, so this would
  still be less than 1ms)

  Option 2:
  Sort the string (nlogn) then compare a char's index before sorting to its
  index after; still likely to devolve to n^2
*/

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
  if (a.first != b.first) {
    return a.first < b.first;
  } else {
    return a.second < b.second;
  }
}

int score(const string &dna, const int length) {
  int score = 0;
  for (int i = 0; i < length; i++) {
    for (int j = i + 1; j < length; j++) {
      if (dna[i] > dna[j]) {
        score++;
      }
    }
  }

  return score;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int stringsLen;
  int stringsCount;
  cin >> stringsLen >> stringsCount;
  vector<string> strings;
  vector<pair<int, int> > scoreStrings;
  rep(i, stringsCount) {
    string dna;
    cin >> dna;
    strings.push_back(dna);
    scoreStrings.push_back(pair<int, int>(score(dna, stringsLen), i));
  }

  stable_sort(scoreStrings.begin(), scoreStrings.end(), cmp);

  rep(j, stringsCount) { cout << strings[scoreStrings[j].second] << endl; }
  return 0;
}
