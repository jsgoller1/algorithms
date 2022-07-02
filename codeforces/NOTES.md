## Shortening code

Have ready-to-go preprocessor macros to define common types / operations you will need; see `template.cpp`. Example:

```cpp
#define ll long long
#define var_in(type, var) type var; cin >> var;
#define lin(var) var_in(ll, var)
```

## Easy I/O

I got burned using `scanf()` to read whitespace-separated input (ull not supported), but this worked well:
```c++
unsigned long long m, n, a;
cin >> m >> n >> a;
```

## Pattern matching strings
You can sometimes get away with using `sscanf()` for pattern matching. [1B - Spreadsheets](https://codeforces.com/contest/1/problem/B) presents two different formats for specifying a cell in a spreadsheet: either `^[A-Z]+[0-9]+\$` (e.g. `BB352`) or `^R[0-9]+C[0-9]+\$` (e.g. `R253C55`), and instructs to convert input lines from one form into the other. My first attempt involved writing rule-based parser (the first has no letters after the first number, but the second one always does), which was messy and error prone. A better way to do this is:
```cpp
int x, y;
cin >> input_str;
if (sscanf(input_str, "%*c%d%*c%d", &x, &y) == 2){
    // do conversion for ^R[0-9]+C[0-9]+$
} else {
    // do ^[A-Z]+[0-9]+$ conversion
}

```
The format string `"%*c%d%*c%d"` reads and ignores any number of non-numeric characters with `%*c` while reading and saving the numeric ones via `%d`. An added bonus here is that for a successful match, we automatically store the numeric portion (needed for the conversion), and additionally we still get the numeric portion on in `x` a failed match (while `y` becomes useless). 


## A quick test for evenness:
```cpp
(val & 1) ? /* is even */ : /* is odd */;
```

## Integer types

(WIP section)

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

