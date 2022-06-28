#include <iostream> 
using namespace std;

int main(){
    char c = 0;
    unsigned char uc = 0;
    signed char sc = 0;
    short s = 0;
    unsigned short us = 0;
    signed short ss = 0;
    int i = 0;
    unsigned int ui = 0;
    signed int si = 0;
    long l = 0;
    unsigned long ul = 0;
    signed long sl = 0;
    long long ll = 0;
    unsigned long long ull = 0;
    signed long long sll = 0;

    cout << "sizeof(char): " << sizeof(c) << endl;
    cout << "sizeof(short): " << sizeof(s) << endl;
    cout << "sizeof(int): " << sizeof(i) << endl;
    cout << "sizeof(long): " << sizeof(l) << endl;
    cout << "sizeof(long long): " << sizeof(ll) << endl;

    cout << "Max val - unsigned char: " << (unsigned char)(~uc) << endl; // will ascii character with code 0xff
    cout << "Max val - unsigned short: " << (unsigned short)(~us) << endl;
    cout << "Max val - unsigned int: " << (~ui) << endl;
    cout << "Max val - unsigned long: " << (~ul) << endl;
    cout << "Max val - unsigned long long: " << (~ull) << endl;

    cout << "Range, signed char: " << (signed char)(~sc) << " " << ((~sc)>>1) << endl;
    cout << "Range, signed short: " << (signed short)(~ss) << " " << (signed short)((~ss)>>1) << endl;
    cout << "Range, signed int: " << (signed int)(~sl) << " " << ((~si)>>1) << endl;
    cout << "Range, signed long: " << (signed long)(~((~0)>>1)) << " " << (signed long)((~sl)>>(signed long)1) << endl;
    cout << "Range, signed long long: " << (signed long long)(~sll) << " " << ((~sll)>>1) << endl;

    return 0;
}