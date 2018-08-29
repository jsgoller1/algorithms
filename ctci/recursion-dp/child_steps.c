#include <stdio.h>
#include <stdlib.h>
#define MAX_MEMORY 4096

/*
 * A child is hopping up n steps, and may hop 1, 2, or 3 steps at a time. How
 * many possible ways can the child reach the nth step?
 */

int steps(signed long* map, signed long n)
{
	//printf("Called with: %ld\n", n);
	if (n >= MAX_MEMORY)
	{
		return -1;
	}
	if (n < 0)
		return (signed long) 0;
	else if (n == 0)
		return (signed long) 1;
	else if (map[n] > 0)
		return map[n];
	else
	{
		//printf("%ld call, calling %ld, %ld, %ld\n", n, n-1, n-2, n-3);
		map[n] = steps(map, n-1) +
			steps(map, n-2) +
			steps(map, n-3);
		return map[n];
	}
}

void main(int argc, char* argv[])
{
	if (argc == 1)
		printf("use: ./child_steps <int>\n");
	else
	{
		signed long n = strtol(argv[1], NULL, 0);
		// printf("nth step: %ld\n", n);
		signed long* map = calloc(MAX_MEMORY, sizeof(signed long));
		signed long how_many = steps(map, n);
		if (how_many == -1)
		{
			printf("Exceeded memory boundary, quitting\n");
			printf("Increase MAX_MEMORY (line 3) and recompile\n");
		}
		else
			printf("Number of ways: %lu\n", how_many);
		free(map);
	}
}
