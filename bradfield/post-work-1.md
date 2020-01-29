# Class 1 Postwork

## Part 1

Write a function, `checkPartitionBalance` that takes the following two parameters:

- An input array
- A quicksort partition function (pass the function itself as a parameter)

Call the partition function to obtain two subarrays (`left` and `right`), then return the "relative size" of the smaller subarray.

For example, if `len(left) == 6` and `len(right) == 4`, then return `4 / (6 + 4)`, i.e. `0.4`.

What would you expect `checkPartitionBalance` to return for "good" and "bad" partition functions?

## Part 2

We discussed the test case `[5, 5, 5, 5, 5, 5, 5, 5, 5, 5]` in class.  Come up with at least five more test cases that could plausibly cause `checkPartitionBalance` to return a "bad" value for a naively implemented partition function.

## Part 3

Implement an improved partition function using the "fat pivot" idea from exercise 11 in Column 11 of Programming Pearls (see attached). (By the way, congratulations to those of you who came up with this idea on your own during yesterday's class!)

Call `checkPartitionBalance` using your test cases (from Part 2) and your improved partition function.  How does your improved implementation compare to a naive implementation?

## Part 4

Read page 120 of Programming Pearls (see attached), which describes another idea for an improved partition function.  Once you understand the idea, translate the pseudocode into an actual implementation and test your implementation against `checkPartitionBalance`.

- How does the "two-sided partitioning" strategy compare to the "fat pivot strategy"?

## Part 5

What invariant does Go's `sort.Sort` use when partitioning?

Read the comment on lines 107-113 of this file: https://golang.org/src/sort/sort.go?#L107 and draw a diagram that visually demonstrates the invariant described.

- Why do you think Go chose this partition strategy?
- What factors, aside from the output of `checkPartitionBalance` performance, would want to consider when choosing a partition strategy?
