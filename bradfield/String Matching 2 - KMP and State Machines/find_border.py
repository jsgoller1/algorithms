"""
Let’s define a border of a string to be a proper prefix that’s also a proper suffix (“proper”
means the prefix / suffix isn’t allowed to be the entire string). Write a function that takes
a string and returns the length of its longest border. For example, the string "aabbaa" has two
borders: "a" and "aa", so its longest border has length 2. Don’t worry about efficiency for now.

In: string
out: int
Constraints: string can be very long
----
If "border" means what it says above, I think we can just start comparing the first character to the last character
and stop when we hit a mismatch. We can do this with indexes in the string denoting the end of the prefix and the start
of the suffix.

What are some edge cases?
"" -> 0 (no border)
"a" -> 0 (can't be entire string)
"aa" -> 1, "a"
"aaba" -> 1, "a"
"catak" -> 0
------
"""


def find_border(string):
    if not string:
        return 0
    border_len = prefix = 0
    suffix = len(string) - 1
    while string[prefix] == string[suffix] and prefix < suffix:
        border_len += 1
        suffix -= 1
        prefix += 1
    return border_len


if __name__ == "__main__":
    assert find_border("") == 0
    assert find_border("a") == 0
    assert find_border("aa") == 1
    assert find_border("aaa") == 1
    assert find_border("aaba") == 1
    assert find_border("catak") == 0
