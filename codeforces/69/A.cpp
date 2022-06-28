#include <iostream>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();
    iin(lines_n);
    int x = 0, x_t = 0, y = 0, y_t = 0, z = 0, z_t = 0;
    while(cin >> x >> y >> z){
        x_t += x;
        y_t += y; 
        z_t += z;
    }
    cout << (x_t | y_t | z_t ? "NO" : "YES") << endl;
    return 0;
}