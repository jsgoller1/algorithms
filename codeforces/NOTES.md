A quick test for evenness:
```cpp
(val & 1) ? /* is even */ : /* is odd */;
```
---

When choosing a numeric type, make sure problem bounds won't overflow it. For C++ (per Stroustrup),
the size of numeric types is machine specific with some assurances:
- `1` ≡ `sizeof(char)` ≤ `sizeof(short)` ≤ `sizeof(int)` ≤ `sizeof(long)` ≤ `sizeof(long long)`
- `sizeof(float)` ≤ `sizeof(double)` ≤ `sizeof(long double)`
- `sizeof(N)` ≡ `sizeof(signed N)` ≡ `sizeof(unsigned N)`

Integer sign is determined via [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement), so the value range of signed types will be less than the unsigned variant of the same type, despite being the same size. If we assume a `char` is 8 bits and signed by default, the we can use the following back-of-the-envelope estimations (specifically underestimates to avoid overflow):


| Type                                           | Bytes   | Bits            | Min val                    | Max val                    | Ballpark range  |
|------------------------------------------------|---------|-----------------|----------------------------|----------------------------|-----------------|
| char                                           | 1       | 8               | -127                       | 127                        |    duh          |
| unsigned char                                  | 1       | 8               | 0                          | 255                        |    duh          |
| short (int)                                    | 2       | 16              | -32,767                    | 32,767                     | 0 to 3*(10^4)   |
| unsigned short (int)                           | 2       | 16              | 0                          | 65,535                     | 0 to 6*(10^4)   |
| int                                            | 4       | 32              | -2,147,483,647             | 2,147,483,647              | ±2 * (10^9)     |
| unsigned (int)                                 | 4       | 32              | 0                          | 4,294,967,295              | 0 to 4 * (10^9) |
| long (int) / long long (int)                   | 8       | 64              | -9,223,372,036,854,770,000 | 9,223,372,036,854,770,000  | ±9 * 10^18      |
| unsigned long (int) / unsigned long long (int) | 8       | 64              | 0                          | 18,446,744,073,709,500,000 | 0 to 10^19      |


(note that `long long` and `long` have the same size here; this is machine specific, but valid according to Stroustrup).

---

Have ready-to-go preprocessor macros to define common types / operations you will need; see `template.cpp`. Example:

```cpp
#define ll long long
#define var_in(type, var) type var; cin >> var;
#define lin(var) var_in(ll, var)
```
---

I got burned using `scanf()` to read whitespace-separated input (ull not supported), but this worked well:
```c++
unsigned long long m, n, a;
cin >> m >> n >> a;
```