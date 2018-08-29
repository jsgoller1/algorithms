#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Simple string reveral; take a string, allocate new memory for it,
// then parse the old string backwards and copy it into the new array.

char* string_reverse(char* fwd);

char* string_reverse(char* fwd){
	signed int fwd_len, rev_len;
	fwd_len = rev_len = 0;
	while(*(fwd+fwd_len)){ // If I ever care enough, this is probably better done with strlen
		fwd_len++;
	}
	char* reversed = malloc(fwd_len);
	fwd_len--; // don't want to copy null terminator
	while(fwd_len >= 0){
		reversed[rev_len] = fwd[fwd_len];
		fwd_len--;
		rev_len++;
	}
	reversed[++rev_len] = "\0";
	return reversed;
}

void main() {
	char fwd[] = "This is the forward string";
	char* reversed;
	printf("string: %s \n", fwd);
	reversed = string_reverse(fwd);
	printf("string: %s \n", reversed);
	free(reversed);
}
