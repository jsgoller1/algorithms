#include <iostream>
#include <map>

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
    iin(lines);
    string curr;
    map<string, int> names;
    while (cin >> curr){
        if (names[curr] == 0){
            names[curr] = 1;
            output("OK");
        } else {
            output(curr << names[curr]++);
        }
    }
    return 0;
}