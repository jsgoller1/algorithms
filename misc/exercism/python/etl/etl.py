"""
See README for problem statement.
---
Understand - For this problem, we
are trying to transform data in one format into
data in another format. The input is a dictionary
mapping ints to a list of characters, and the output
needs to be a dictionary mapping chars to ints.
----
Plan - To solve this, we need to get the list associated
with each integer key, and then iteratively map each item
in the list (in lowercase) to the int the new dictionary.
----
Execute - see below.
----
Review: The space and time complexity of this program is O(c) - since
the new dictionary always has a mapping of letters to scores,
it will always contain 26 elements. Additionally, we will never need
to examine more than 26 letters in the transform process, so it takes
constant time to complete.
"""


def transform(legacy_data):
    new_mapping = {}
    for old_key in legacy_data.keys():
        for old_letter in legacy_data[old_key]:
            new_mapping[old_letter.lower()] = old_key

    return new_mapping
