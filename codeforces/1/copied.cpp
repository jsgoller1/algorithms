// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

#include <cstdio>
void g(int t) {
  /*
  This recursive helper procedure converts a decimal number to Excel column
  alphabetical format; the Excel format can be thought of as a base-26 number
  system (with A = 1, B = 2, ..., Z = 26), but it has an important difference.

  Normally, we can convert from a lower base to a higher one via successive
  division is 0; the remainder after each step are the characters in the new
  base, starting with the least significant. Suppose we want to convert decimal
  12345 to hexidecimal (which will be 0x3039):

  12345 / 16 = 771    12345 % 16 = 9
    771 / 16 = 48       771 % 16 = 3
     48 / 16 = 3         48 % 16 = 0
      3 / 16 = 0          3 % 16 = 3

  However, this procedure won't work for our Excel format with base 26. Try
  using it to convert decimal 494; the result should be "RZ", but we wind up
  with "?S":

   494 / 26 = 19    494 % 26 = 0   // ?; we have no letter for 0
    19 / 26 = 0      19 % 26 = 19  // S; A = 1, B = 2, ... , S = 19

  We have two problems:
  - No zero
  - Off-by-one; Excel format treats A as the first symbol in the number system
    but uses A = 1. In decimal, "1" is the second character, after "0" - so when
    n % 26 == 1 in our procedure, it really means "use the second character".

  However, suppose we make two slight adjustments:
  - Each time we do a subsequent division,
  - Whenever we have N % 26 == 0, emit "Z"

  */
  if (t) {  // base case t == 0; terminates recursion
    g((t - 1) / 26);
    putchar(65 + (t - 1) % 26);
    /* the last recursive call will return first and evaluate
       the most significant character, so having putchar() after
       the recursive call ensures the most significant char is
       printed first.
    */
  }
}

int main() {
  int n, x, y;
  char s[64], *p;
  for (scanf("%d ", &n); n--;) {
    gets(s);
    if (sscanf(s, "%*c%d%*c%d", &x, &y) == 2) {
      // RC to Excel
      // y contains col number as numeric, needs to be converted to alphabetical
      g(y);
      // x contains row number and can be printed directly
      printf("%d\n", x);
    } else {
      // Excel to RC
      // sscanf() returns 0, so x and y uninitialized
      // Initialize x to 0 so we can use it for storing the columns portion
      for (x = 0, p = s; *p > 64; ++p) {
        /*
          p is initially set to first char of s (first letter, chars between 64
          for A and 90 for Z); go through chars and stop when we reach one
          outside the 64-90 range, indicating it's a number. p will then point
          at the first numeric character of the rows portion, so we can use it
          in printing the R-C form output.
        */
        x = x * 26 + *p - 64;
        /*
          Conversion of alphabetical chars to base-10 int
          We can map A=1, B=2, etc by taking the ASCII char value and
          subtracting 64, then using it as a power of 26.
          Example: RZA228 -> R228C12845
          Col portion: RZA -> 12845
          (('R' - 64) * 26^2) + (('Z' - 64) * 26^1) + (('A' - 64) * 26^0)
          (18 * 26^2) + (26 * 26) + (1 * 1)
          12168 + 676 + 1 = 12845

          However, this program instead obtains the result by repeatedly
          calculating x = x * 26 + *p - 64. My first impression looking at this
          was "wtf?"

          First, what does it actually do? Parenthesize for explicit order of
          operations:
          1) Dereference: x*26+(*p)-64
          2) Multiplication: (x*26)+(*p)-64
          3) Add / sub, with L-to-R associativity: ((x*26)+(*p))-64
          (ref: https://en.cppreference.com/w/cpp/language/operator_precedence)

          Then via substitution, we can write the entire loop for RZA -> 12845
          as a single calculation and evaluate it to see it gives the correct
          result:
          (((((((((0*26)+(82))-64)*26)+(90))-64)*26)+(65))-64)
          or equivalently
          ((((0*26)+(82-64))*26+(90-64))*26+(65-64))
          ((((0)+(18))*26+(26))*26+(1))
          ((18*26+(26))*26+(1))
          ((468+26)*26)+1
          12845

          Why is it equivalent to the first method using powers of 26? We can
          factor one into the other:
          ((((0*26)+(82-64))*26+(90-64))*26+(65-64))
               ^------drop since it evaluates to 0
          (((82-64)*26+(90-64))*26+(65-64))
                                ^--- distribute over inner expression
          (82-64)*26^2 + (90-64)*26 + (65-64)*26^0
                                                ^---26^0=1, so
                                                    (65-64)*26^0=(65-64)
        */
      }
      printf("R%sC%d\n", p, x);
    }
  }
  return 0;
}
