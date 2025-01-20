from test_framework import generic_test


def is_palindrome_number_string(x: int) -> bool:
    if x < 0:
        return False 
    string = str(x)
    l, r = 0, len(string)-1
    while l < r: 
        if string[l] != string[r]:
            return False 
        l, r = l+1, r-1 
    return True

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False 
    left_place = right_place = 1
    while x // (left_place * 10):
        left_place *= 10
    while left_place > right_place: 
        if x//left_place%10 != x//right_place%10:
            return False 
        left_place, right_place = left_place//10, right_place*10 
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
