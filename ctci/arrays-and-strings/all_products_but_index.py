"""
Given an array of integers, return an array that contains the product of every
int in the array except the one at the index. For example, the array
[1,2,3,4,5] should return [120, 60, 40, 30, 24], i.e.
120 = 2*3*4*5
60 = 1*3*4*5
40 = 1*2*4*5
30 = 1*2*3*5
24 = 1*2*3*4

Solution:
There are three ways to solve this problem. The first one is a O(n^2) solution
that involves linearly stepping through the array, and the calculating the
product of all of the other numbers at each step. This is too slow.

The first O(n) solution involves division - simply calculate the product of
every entry in the array, then step through it again, dividing the total
by array[i] and storing the result in solution[i]. This requires us to handle
zeros carefully, though, so there will be some extra computation involve (but
still O(n)).

The second O(n) solution involves parsing through the array forwards,
calculating the product of each entry up to that index, and then stepping
through it backwards and doing the same. In my opinion, this is unnecessarily
convoluted and has a minimal performance gain.

By convention, we assume:
The total product of an empty array is an empty array.
The total product of a 1 element array is [1].
The total product of a 2 element array is simply the array.
"""
import random
import copy

def array_product_method_1(array):
    zeroes = array.count(0)
    solution = []
    total_product = 1
    if zeroes == 0: # we're safe from division by zero
        for each in array:
            total_product *= each
        for each in array:
            solution.append(total_product / each)
    elif zeroes == 1: #everything in the array will be zero except array.index(0)
        # copy the original array, and remove the zero
        no_zero = copy.deepcopy(array)
        no_zero.remove(0)
        # calculate the total product of everything but the zero
        for each in no_zero:
            total_product *= each
        # Fill the solution array with 0s, then place the total product in
        # the same place where 0 was in the input array.
        for each in array:
            solution.append(0)
        solution[array.index(0)] = total_product
    else: # if there's two 0s, then the total product of everything is 0
        for each in array:
            solution.append(0)
    return solution

# This was the solution presented on interviewcake.com; I wouldn't use it.
def array_product_method_2(array):
    if len(array) == 0 or len(array) == 2:
        return array
    if len(array) == 1:
        return [1]

    # Dummy array
    products = [1] * len(array)

    # first, parse right and calculate products[i] as "the product of all
    # values to the left of products[i]"
    total_product = 1
    index = 0
    while index < len(array):
        products[index] = total_product
        total_product *= array[index]
        index+=1

    # now, do the same thing, but go from right to left, and multiply
    # values with the previous ones
    total_product = 1
    index = len(array) - 1
    while index >= 0:
        products[index] *= total_product
        total_product *= array[index]
        index -= 1

    return products

if __name__ == "__main__":
    array = [1,2,3,4,5]
    print "Original array:", array
    solution = array_product_method_1(array)
    print "Solution:"
    print solution
    array = [1,2,3,4,0]
    print "Original array:", array
    solution = array_product_method_1(array)
    print "Solution:"
    print solution
    array = [0,2,3,4,0]
    print "Original array:", array
    solution = array_product_method_1(array)
    print "Solution:"
    print solution
