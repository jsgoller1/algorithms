import library

instructions = """
Examples of spiral-form printing:

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

"""

def spiral_print(matrix):
    x_left = y_top = 0
    x_right = len(matrix[0])
    y_bottom = len(matrix)
    print_list = []
    while (x_left < x_right):
        #print("parse right")
        for each in range(x_left, x_right):
            print_list.append(matrix[y_top][each])
        #print "\n"
        y_top += 1

        #print("parse down")
        for each in range(y_top, y_bottom):
            print_list.append(matrix[each][x_right-1])
        #print "\n"
        x_right -= 1

        #print("parse left")
        for each in reversed(range(x_left, x_right)):
            print_list.append(matrix[y_bottom-1][each])
        #print "\n"
        y_bottom -= 1

        #print("parse up")
        for each in reversed(range(y_top, y_bottom)):
            print_list.append(matrix[each][x_left])
        #print "\n"
        x_left += 1
    print print_list

if __name__ == "__main__":
    if (raw_input("Print instructions (y/n) ?") == "y"):
        print instructions
    matrix = library.generate_matrix()
    print "Matrix: "
    library.show(matrix)
    print("Spiral ordered print:")
    spiral_print(matrix)
