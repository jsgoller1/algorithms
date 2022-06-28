#include <iostream>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();

    /* 
        - One pass r-to-l, keeping running sum and counter mapping sum to number of times the running sum has been this value
        - initialize "total ways" to 0
        - one pass l-to-r, keeping running sum. at each step, check if array's sum equals 3 times current sum; if so, look up current sum in counter, add result to total ways
    */

    return 0;
}