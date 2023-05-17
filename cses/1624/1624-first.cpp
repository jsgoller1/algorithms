// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

// Includes all standard headers (no need for <vector>, <list>, etc).
#include <bits/stdc++.h>

using namespace std;

// --- I/O ---
/*
sync_with_stdio(): do not sync C++ streams (e.g. std::cin) with C streams
(e.g. stdin) after each output; adds unnecessary time.

tie(): untie cin from cout (tied by default); if tied, each read from cin
flushes cout, adds unnecessary time. Unclear from Stroustrup if both need to be
untied, doing it to be safe.
*/
#define sanic_io()                  \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL);                    \
  cout.tie(NULL);
#define endl "\n"  // std::endl causes a flush, adds unnecessary time
#define read_from_files(in_path, out_path) \
  freopen(in_path, "r", stdin);            \
  freopen(out_path, "w", stdout);
#define output(val) cout << val << endl;
#define var_in(type, var) \
  type var;               \
  cin >> var;
#define chin(var) var_in(char, var)
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)

// --- Abbreviations --
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep1(i, n) for (int i = 1; i <= (n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()  // reverse iterator
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define mp make_pair

// -- Types --
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;

// -- Testing --
#ifdef LOCAL
#define eprintf(...)              \
  {                               \
    fprintf(stderr, __VA_ARGS__); \
    fflush(stderr);               \
  }

#else
#define eprintf(...) 0
#endif

#define QUEEN_COUNT 8
#define BOARD_HEIGHT 8
#define BOARD_WIDTH 8

// Row / Y is first, col / X is second
typedef pair<int, int> boardLocation;

void getInput(vector<boardLocation>& blockedSpaces) {
  for (int y = 0; y < BOARD_HEIGHT; y++) {
    for (int x = 0; x < BOARD_WIDTH; x++) {
      chin(space);
      if (space == '*') {
        blockedSpaces.push_back(boardLocation(y, x));
      }
    }
  }
}

bool sameRow(const boardLocation& queen1, const boardLocation& queen2) {
  return queen1.first == queen2.first;
}

bool sameCol(const boardLocation& queen1, const boardLocation& queen2) {
  return queen1.second == queen2.second;
}

bool sameDiag(const boardLocation& queen1, const boardLocation& queen2) {
  return abs(queen1.first - queen2.first) == abs(queen1.second - queen2.second);
}

bool canAddPlacement(const boardLocation& possible,
                     const set<boardLocation>& placedQueens) {
  // If any two queens are on the same row or column, the placement is
  // invalid
  for (auto current : placedQueens) {
    if (sameRow(current, possible) || sameCol(current, possible) ||
        sameDiag(current, possible)) {
      return false;
    }
  }
  return true;
}

bool spaceNotBlocked(const boardLocation& possible,
                     const vector<boardLocation>& blockedSpaces) {
  // Check if this space is blocked
  for (auto blocked : blockedSpaces) {
    if (blocked == possible) {
      // printf("Cannot place at (%d, %d), blocked.\n", possible.first,
      //       possible.second);
      return false;
    }
  }
  return true;
}

void generateSolutions(set<set<boardLocation>>& knownSolutions,
                       set<boardLocation>& placedQueens,
                       const vector<boardLocation>& blockedSpaces) {
  if (placedQueens.size() == QUEEN_COUNT) {
    /*
    printf("Found solution: ");
    for (auto loc : placedQueens) {
      printf("(y: %d, x: %d), ", loc.first, loc.second);
    }
    printf("\n");
    */
    knownSolutions.insert(placedQueens);
  }

  for (int y = 0; y < BOARD_HEIGHT; y++) {
    for (int x = 0; x < BOARD_WIDTH; x++) {
      boardLocation newLoc(y, x);
      // Add queen if possible and proceed with solution generation
      // printf("(%d, %d) not blocked.\n", newLoc.first, newLoc.second);
      if (spaceNotBlocked(newLoc, blockedSpaces) &&
          canAddPlacement(newLoc, placedQueens)) {
        placedQueens.insert(newLoc);
        generateSolutions(knownSolutions, placedQueens, blockedSpaces);
        placedQueens.erase(newLoc);
      }
    }
  }
}

int main() {
  sanic_io();
  set<set<boardLocation>> knownSolutions;
  set<boardLocation> placedQueens;
  vector<boardLocation> blockedSpaces;
  getInput(blockedSpaces);
  /*
  for (auto space : blockedSpaces) {
    printf("Blocked: (%d,%d)\n", space.first, space.second);
  }
  */

  generateSolutions(knownSolutions, placedQueens, blockedSpaces);
  // printf("%d\n", knownSolutions.size());
  // printf("\n");
  /*
  for (auto solution : knownSolutions) {
    printf("[");
    for (auto cell : solution) {
      printf("(%d, %d), ", cell.first, cell.second);
    }
    printf("],\n");
  }
  */
  return 0;
}
