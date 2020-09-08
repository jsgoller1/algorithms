"""
See README.md for problem statement.
-----------
Understand - The problem calls for a program that takes a matrix string and
from it is able to construct a matrix data type that can return arbitrary
rows or columns. Looking at the tests, the matrix string is given to the
constructor as a string of newline-or-whitespace separated characters,
and then arbitrary rows and columns are retrieved via a row()
method and a column() method, each of which take an index
as an argument and return a list representing that row or column.
Depending on which method is called, we must return the correct
elements from the matrix that is represented by the string.

-----
Plan

The solution to this problem depends on:
- parsing the matrix string correctly
- storing the data in a way that makes fetching row and column data easy.

Parsing the string: based on the values given to the constructors in the test file,
rows will be separated by newlines. Thus, we can go value by value appending items
to a row until we encounter a newline, at which point we should create a new row
and continue parsing values from the string.

(When I went to implement this, I took a slightly different approach on realizing that the
matrix_string.split('\n') returned a list of strings, which are then able to be split() on
whitespace - I was able to save effort by doing this with a list comprehension)

Storing the data: in Python a matrix
is usually represented as a list of lists, where each sublist is a row. We can begin
with an empty top-level list and one sublist - as we read in values, we can append them to our
sublist; once a newline is read, append the sublist to the top-level list, create a new
sublist, and continue reading values. Do this until we exhaust the matrix string.

For fetching rows, we can just return the specific index of a row in the top-level list
of the Matrix type.

For fetching columns with column(i), we can construct a list by looping through the top level
list of Matrix, getting the i-th item of each row, and
---
Execute - see below.
---
Review - The space complexity of the matrix constructor is O(N) for a matrix of N elements; no additional
space is needed to store meta-data. row() and column() will both return 1/N elements, so their
space complexity is also O(N).

The the constructor runs split(), will need to check every character in the string (M steps for a string of length M).
Then, each substring must be split on whitespace, which takes another M steps (technically less because we've removed
the newline characters). Finally, each non-whitespace character is then added to an array, so this is M steps minus
the number of whitespaces minus the number of newlines, so probably around M/2. As such the constructor should take
M + M + M/2 steps, which should be O(M).

row() is O(c) since it's just a retrieval of a value at an array index.

column() is O(1/N) for an N x N matrix, and thus O(N).
"""


class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = []
        matrix_list = matrix_string.split('\n')
        for row_string in matrix_list:
            row_list = [int(num) for num in row_string.split(' ')]
            self.rows.append(row_list)

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return [row[index] for row in self.rows]
