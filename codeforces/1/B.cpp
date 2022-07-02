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

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

static int exp26(int pow) {
  switch (pow) {
    case 0:
      return 1;
    case 1:
      return 26;
    case 2:
      return 676;
    case 3:
      return 17576;
    case 4:
      return 456976;
    default:
      return -90000000;
  }
}

static void solve() {
  strin(cell);
  bool found_int = false, is_excel = true;
  rep(i, (int)cell.size()) {
    char c = cell[i];
    if ('0' <= c && c <= '9') {
      found_int = true;
    } else {
      is_excel = !found_int;
    }
  }

  if (is_excel) {
    int first_i = 0;
    while ('A' <= cell[first_i] && cell[first_i] <= 'Z') {
      first_i++;
    }
    string row = cell.substr(first_i);
    int col = 0;
    int last_a = first_i - 1;
    for (int pow = 0; last_a >= 0; last_a--) {
      col += (cell[last_a] - 64) * exp26(pow);
      pow++;
    }
    output("R" << row << "C" << col);

  } else {
    /*
     R*C* to Excel
      int row = read after R until C, then atoi() it
      str col = read from C to end
      return base26_encode(row) + col
    */
    int c_i = 0;
    while (cell[c_i] != 'C') {
      c_i++;
    }
    string row = cell.substr(1, c_i - 1);
    int col_val = stoi(cell.substr(c_i + 1));
    string col;
    while (col_val > 0) {
      int next_offset = 0;
      int offset = (col_val % 26);
      if (offset == 0) {
        offset = 26;
        next_offset = 1;
      }
      char next_char = (char)(64 + offset);
      col.insert(col.begin(), next_char);
      col_val = (col_val / 26) - next_offset;
    }
    output(col << row);
  }
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  //  read_from_files();
  lin(cases);

#ifdef LOCAL
  start_time = getCurrentTime();
  rep(i, cases) {
    case_time = getCurrentTime();
    solve();
    eprintf("Case %d: %f sec \n", i, getCurrentTime() - case_time);
  }
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#else
  rep(i, cases) { solve(); }
#endif

  return 0;
}
