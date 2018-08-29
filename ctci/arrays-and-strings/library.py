import random

"""
Creates a string of '1's or '0's. Length is randomly chosen if not provided.
"""
def generate_binstring(n=random.randint(1,50)):
    string = ''
    for each in range(n):
        if random.getrandbits(1):
            string += '1'
        else:
            string += '0'
    return string

"""
Generates an n by n matrix represented by a list of lists. n will be randomly
chosen if not provided.
"""
def generate_matrix(n=random.randint(1, 11)):
    matrix = [[] for i in range(n)]
    for row in matrix:
        for column in range(n):
            row.append(random.randint(0,9))
    return matrix

"""
Borrowed this function from some code I was given for a Udacity project.
I don't entirely understand lambda function syntax for Python yet, but all
show() does is nicely display a grid that is represented using lists of lists
"""
def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:d}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    print("\n")

