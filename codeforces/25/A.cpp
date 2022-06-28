#include <iostream>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();
    iin(lines_n);
    int odds_n = 0, last_odd_i = 0, evens_n = 0, last_even_i = 0, curr = 0, curr_i = 1;
    while (cin >> curr){
        if (curr & 1){
            odds_n++;
            last_odd_i = curr_i;
        } else {
            evens_n++;
            last_even_i = curr_i;
        }
        curr_i++;
    }
    cout << ((odds_n == 1) ? last_odd_i : last_even_i) << endl;
    return 0;
}