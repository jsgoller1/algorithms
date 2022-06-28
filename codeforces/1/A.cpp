#include <iostream>

using namespace std;

int main(){
    unsigned long m, n, a;
    cin >> m >> n >> a;
    cout << ((m/a) + (m % a ? 1 : 0)) * ((n/a) + (n % a ? 1 : 0)) << endl;
    return 0;
}