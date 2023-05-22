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

ll findMaxAvailableTicket(ll startPosition,
                          const vector<pair<ll, ll>>& tickets) {
  for (ll idx = startPosition; idx >= 0; idx--) {
    if (tickets[idx].second != 0) {
      return idx;
    }
  }
  return -1;
}

ll findMinAvailableTicket(ll startPosition,
                          const vector<pair<ll, ll>>& tickets) {
  for (ll idx = startPosition; idx < tickets.size(); idx++) {
    if (tickets[idx].second != 0) {
      return idx;
    }
  }
  return -1;
}

ll binSearch(const ll value, const vector<pair<ll, ll>>& values) {
  // Modified for this problem. If:
  // - value exists in values, we will return the idx to it
  // - value does not exist (but at least one less than it does), we
  //   will return the idx of the closest to value less than it
  // - all entrys in value exceed array: we return -1
  if (value < values[0].first) {
    return -1;
  }
  ll lo = 0;
  ll mid = 0;
  ll hi = values.size() - 1;
  while (lo <= hi) {
    mid = (lo + hi) / 2LL;
    if (values[mid].first == value) {
      return mid;
    } else if (values[mid].first < value) {
      lo = mid + 1;
    } else {  // value < values[mid]
      hi = mid - 1;
    }
  }
  return lo - 1;
}

int main() {
  lin(n_tickets);
  lin(m_customers);

  map<ll, ll> ticketCount;
  // printf("Mapping.\n");
  rep(i, n_tickets) {
    lin(ticket);
    auto count = ticketCount.find(ticket);
    if (count == ticketCount.end()) {
      ticketCount[ticket] = 1;
    } else {
      ticketCount[ticket]++;
    }
  }

  // printf("Assembling vector.\n");
  vector<pair<ll, ll>> tickets;
  for (auto curr = ticketCount.begin(); curr != ticketCount.end(); curr++) {
    tickets.push_back(*curr);
  }

  vl customers;
  rep(i, m_customers) {
    lin(customer);
    customers.push_back(customer);
  }

  ll maxAvailable = findMaxAvailableTicket(tickets.size() - 1, tickets);
  ll minAvailable = findMinAvailableTicket(0, tickets);
  for (auto customer : customers) {
    output("Customer: " << customer);
    output("Current max: " << tickets[maxAvailable].first);
    output("Current min: " << tickets[minAvailable].first);
    if (customer < tickets[minAvailable].first) {
      output(-1);
      continue;
    }

    ll idx = binSearch(customer, tickets);
    output("Desired: " << tickets[idx].first);
    idx = (idx > maxAvailable) ? maxAvailable : idx;
    output("Desired (updated): " << tickets[idx].first);

    ll times = 0;
    while (idx >= 0 && tickets[idx].second < 1) {
      idx--;
      times++;
    }
    output("Actual: " << tickets[idx].first);
    output("Had to search through: " << times);
    if (idx == -1) {
      output(-1);
    } else {
      output(tickets[idx].first);
      tickets[idx].second--;
    }
    if (tickets[minAvailable].second == 0) {
      minAvailable = findMinAvailableTicket(minAvailable, tickets);
    }
    if (tickets[maxAvailable].second == 0) {
      maxAvailable = findMaxAvailableTicket(maxAvailable, tickets);
    }
    output("----");
  }

  return 0;
}
