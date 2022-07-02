Editorial for 1B - Spreadsheets
--- 
I didn't like the official explanation for 1B, so here's mine.

## Problem
**Input**: First line is an int representing the number of test cases. Each following line is a string of characters specifying a spreadsheet cell, in one of two formats:
- "Excel": `^[A-Z]+[0-9]+\$` (e.g. `BB352`). 
- "RC": `^R[0-9]+C[0-9]+\$` (e.g. `R253C55`).

**Output**: For test case, we must output the same cell specified in the opposite format.

Example:
```
2
R23C55
BC23
```
should output
```
BC23
R23C55
```

**Constraints**:
- Between 1 and 10000 test cases
- No invalid test cases
- In each case, the row and column numbers are no larger than 1000000

Note that the constraints also imply a maximum line length of 16 since we never exceed R1000000C1000000 (or BDWGN1000000).

## Approach
This problem involves 3 core parts:
- Determine which format the input is in
- Convert from Excel to RC
- Convert from RC to Excel 

## Determine format
Note that for RC format, we will always find a C after some numbers in the string, whereas with Excel we will never find any letters after numbers. We could use this as a test of format with something like
```cpp
bool found_num = false, is_excel = true;
for (char c: in_str){
    if ('0' <= c && c <= '9') {
        found_num = true;
    } else {
        is_excel = !found_num;
    }
}
```

I like this better though, since it does the determination and reads the portions we need to convert, all in one step:
```cpp
int x, y;
if (sscanf(input_str, "%*c%d%*c%d", &x, &y) == 2){
    // do conversion for ^R[0-9]+C[0-9]+$
} else {
    // do ^[A-Z]+[0-9]+$ conversion
}
```

## Excel to RC
The Excel format is a base 26 format based on the alphabet, i.e. A = 1, B = 2, etc. So CBA = `(3 * 26^2) + (2 * 26^1) + (1 * 26^0)`. You may notice that there is no character associated with 0; this will be important later. We can do this conversion as follows:
```
sum = 0, pow = 0
for each char in reversed(string):
    value = lookup(char)
    sum += value * (26^pow)
    pow++
```

We can implement `lookup()` using a hash table, which can be done implicitly via ASCII:
```cpp
char c = 'A';
int i = (int)(c - 64);
```

Calculating powers of 26 is a bit trickier since C++ has no built-in integer exponentiation. We could implement an `exp()` function via:
```cpp
uint exp(uint pow){return (pow ?  26 * exp(pow-1) : 1); }
```
or 
```cpp
uint exp(uint pow) {
    uint sum = 1;
    for (uint i = 1; i <= pow; i++) { sum *= 26;} 
    return sum; 
}
```
The iterative version is slightly faster. Alternatively, we could use a hashtable here too since the problem constraints mean we'll never compute 26^n for n > 4 (though this requires more code):
```cpp
int exp26(int pow) {
  switch (pow) {
    case 0:
      return 1;
    case 1:
      return 26;
    case 2:
      return 676;
    // ...
  }
}
```
