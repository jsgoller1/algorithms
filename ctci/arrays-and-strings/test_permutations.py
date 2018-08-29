"""
Write a program that determines if two strings are permutations of each other.
Assume "Cat" and "cat" are _not_ permutations of each other. Assume zero-length
strings are
"""

def test_permutations(str1, str2):
    # Ignore trivial cases
    if len(str1) != len(str2):
        return False
    if len(str1) == 0 or len(str2) == 0:
        return False
    sorted1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))
    return sorted1 == sorted2

if __name__ == '__main__':
    print test_permutations("cat", "CAT")
    print test_permutations("dog", "dgo")
    print test_permutations("fuck", "fuck")
    print test_permutations("", "f")
