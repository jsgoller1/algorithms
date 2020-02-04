"""

"""


def str_eq(str1, str2):
    """
    Manually compare two strings; I specifically
    wrote this instead of using == to ensure my
    comparison was as brute-force-y as possible.
    """
    if len(str1) != len(str2):
        return False
    for i, _ in enumerate(str1):
        if str1[i] != str2[i]:
            return False
    return True


def substring(possible_substr, super_str):
    """
    Dumb substring test. Try every possible position
    in the superstring for the substring until we either
    reach a match or the end of the superstring.
    """

    # Assume the empty string is a substring of every string.
    if possible_substr == "":
        return 0

    for i, _ in enumerate(super_str):
        if str_eq(super_str[i : i + len(possible_substr)], possible_substr):
            return i
    return -1


if __name__ == "__main__":
    # Basic functionality
    assert substring("", "") == 0
    assert substring("a", "a") == 0
    assert substring("hua", "joshua") == 3
    assert substring("nope", "definitely won't be in this superstring") == -1

    # One bad case
    assert substring("cyberpunk", "cyberpun" * 1000) == -1

    # This case is relatively easy to get around with a simple check
    # that the superstring has enough characters remaining that it could
    # contain the substring, but will cause O(n^2) performance for a basic
    # brute force.
    assert substring("a" * 100, "a" * 99) == -1
