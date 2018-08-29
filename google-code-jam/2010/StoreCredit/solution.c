// Joshua Goller, jsgoller1@gmail.com
// Sept 22, 2014
// Problem text at https://code.google.com/codejam/contest/dashboard?c=351101

#include <stdio.h>
#include <stdbool.h>

void main()
{
	FILE *input;
	FILE *output;
	char input_path[20] = "./input.txt";
	char output_path[20] = "./output.txt";
	bool debug;

	// print debug messages?
	debug = true;

	// Open the files and determine the size of the input. Then malloc and read into the dataBuffer
	input = fopen(input_path, "rb");
	output = fopen(output_path, "w+");
	fseek(input, 0, SEEK_END); // go to EOF
	int size;
	size = ftell(input); // get current file pointer
	fseek(input, 0, SEEK_SET);
	if (debug == true)
	{
		printf("The file is %d bytes long.\n", size);
	}

	void char dataBuffer[size]; //holds chars to be converted to ints
	fscanf(dataBuffer, size, 1, input);

	// First, get the number of cases there will be
	int numberOfCases;
	numberOfCases = dataBuffer[0] - '0'; // the C standard assures this will be correct, see paragraph 2.2.1
	if (debug == true)
	{
		printf("There are %d cases in this file.\n", numberOfCases);
	}

	// Loop through each test case and solve
	while (numberOfCases > 0)
	{
		// First find out how much credit you have
		int credit;
		fread(dataBuffer, sizeof(int), 1, input);
		credit = dataBuffer[2] - '0'; // the C standard assures this will be correct, see paragraph 2.2.1
		if (debug == true)
		{
			printf("In store 1, you have %d credit.\n", credit);
		}
		numberOfCases--;
	}
}
