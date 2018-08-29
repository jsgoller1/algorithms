"""
Examples of spiral-form printing:

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Assumes input is an n x n matrix.

"""
import random

def nicely_print(p):
    rows = ['[' + ','.join(map(lambda x: '{0:d}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    print("\n")

def generate_matrix(n, m):
    matrix = [[] for i in range(n)]
    for row in matrix:
        for column in range(m):
            row.append(random.randint(0,9))

    nicely_print(matrix)
    return matrix

def spiral_print(matrix):
    # catch trivial edge cases
    if matrix = [] or [] in matrix:
        print -1
    if n == 1 or m == 1:
        print matrix

    # use "sentinel values" to determine where the end of the row / column is,
    # then shrink them each time; "x" is "which row" and "y" is "which column"
    first_x = first_y = 0
    last_x = len(matrix[0])-1
    last_y = len(matrix)-1

    # Print forwards, down, back, then up, then shrink our sentinel values; stop
    # when the forward-printing step has nothing left to print
    while first_x <= last_x and first_y <= last_y:
        # forwards
        line = ''
        for val in range(first_x, last_x+1):
            line += str(matrix[first_y][val])
        first_y += 1
        print line

        # Ugly hack to catch edge case for n x m matrix where n < m
        if first_y >= last_y:
            break

        line = ''
        for val in range(first_y, last_y+1):
            line += str(matrix[val][last_x])
        last_x -= 1
        print line

        line = ''
        for val in range(last_x, first_x-1, -1):
            line += str(matrix[last_y][val])
        last_y -= 1
        print line

        # Ugly hack to catch edge case for n x m matrix where n > m
        if first_x >= last_x:
            break

        line = ''
        for val in range(last_y, first_y-1, -1):
            line += str(matrix[val][first_x])
        first_x += 1
        print line


if __name__ == '__main__':
    spiral_print(generate_matrix(5, 5))
