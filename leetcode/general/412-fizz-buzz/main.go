/*
Statement

Write a program that outputs the string representation
of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead
of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five
output “FizzBuzz”.

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

Input: Int, termination point
Output: Array - numbers as strings, fizzes, and buzzes
--------
Understand

- Use modlulus operator, append to empty string, then append to array.

*/
package main

import (
	"bytes"
	"fmt"
	"strconv"
)

func fizzBuzz(n int) []string {
	if n < 1 {
		return nil
	}
	solution := make([]string, n)
	for i := 1; i <= n; i++ {
		var buf bytes.Buffer
		if i%3 == 0 {
			buf.WriteString("Fizz")
		}
		if i%5 == 0 {
			buf.WriteString("Buzz")
		}
		if buf.Len() == 0 {
			buf.WriteString(strconv.Itoa(i))
		}
		solution[i-1] = buf.String()
	}
	return solution
}

func main() {
	fmt.Println(fizzBuzz(0))
	fmt.Println("--------------------")
	fmt.Println(fizzBuzz(-1))
	fmt.Println("--------------------")
	fmt.Println(fizzBuzz(15))
	fmt.Println("--------------------")
	fmt.Println(fizzBuzz(100))
}
