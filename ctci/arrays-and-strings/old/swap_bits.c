#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

/*
Assume your binstring (number) is 10100110 and you want to swap the 0th bit
(least sig) with the 7th bit (most sig). Going with the variable names in
swap_bits(), single1 = 00000001, and single2 = 10000000.

10000000    10000001
OR          XOR
00000001    10100110
========    ========
10000001    00100111

00100111 is 10100110 with bits 0 and 7 swapped. The check for bit sameness
is relatively simple. Assume that instead we want to swap bits 0 and 7 in
the number 10000001. Then single1 and single2 will be the same as in
the example above, and:

10000000   000000001
NOT        NOT
========   =========
01111111   111111110

Both of these values OR'd with the number produce 11111111, indicating that they
are the same bit and thus swapping them would have no effect, so swap_bits()
returns number unchanged.
*/

int swap_bits(int number, int bit1, int bit2)
{
	int single1, single2;
	single1 = 1 << bit1;
	single2 = 1 << bit2;
	if((number | ~single1) == (number | ~single2))
	{
		printf("Bits %d and %d are the same.\n", bit1, bit2);
		return number;
	}
	number ^= (single1) | (single2);
	return number;
}

bool main()
{
	srand(time(NULL));
	int number, newnumber, i, j;
	i = rand() % 31;
	j = rand() % 31;
	number = rand();

	// i = 0;
	// j = 31;
	// number = (1 << 31) + 1;
	
	if (i == j)
	{
		printf("i and j are equal, quitting...");
		return false;
	}
	
	printf("Swapping bits %d and %d (zero indexed) in 0x%x\n", i, j, number);
	newnumber = swap_bits(number, i, j);
	printf("0x%x\n", newnumber);
}
