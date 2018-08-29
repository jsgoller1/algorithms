## Problem statement
# Given an array of integers, return whether or not there's an integer that
# appears twice in the array

## Solutions
# Efficient approach: use a hashmap
def contains_duplicate(arr):
    print arr
    # Exclude trivial cases
    if arr == []:
        return False
    # type: (int) -> bool
    duplicates = {}
    for each_int in arr:
        try:
            if duplicates[str(each_int)] == True:
                return True
        except KeyError:
            duplicates[str(each_int)] = True
    return False

## Problem statement
# Extending on the first problem, return true if there are indexes i, j such that:
# arr[i] == arr[j] and |i - j| <= k

## Solution
# Keep a dictionary but hash to the most recently seen index instead of a bool.
# Suppose k is 3
# {"1": 3} # 1 exists at arr[3]
# Later see 1 at arr[15]
# 15 - 3 = 12, greater than k, continue
# # And then later see 1 at arr[18] - most recent is 15, so this should cause True

def contains_duplicate_within_k(arr, k):
    print arr
    # Exclude trivial cases
    if arr == []:
        return False
    if k == 0:
        return False
    # type: (int) -> bool
    duplicates = {}
    for idx, each_int in enumerate(arr):
        try:
            # Subtraction comparison / ditch old value
            if idx - duplicates[str(each_int)] <= k:
                return True
            else:
                duplicates[str(each_int)] = idx
        except KeyError:
            # If we haven't seen value before, just store index
            duplicates[str(each_int)] = idx
    return False


## Problem statement
# Extending on the last one, assume that two values are neighbors iff |x - y| <= delta
#
# Want to return true if:
# There are two indexes i, j (not equal) such that:
# - |arr[i] - arr[j]| <= delta
# - |i - j| <= k

# Note that this function is incomplete.
# contains_neighbors_within_k_delta([1,200,3,4,5,62,7,85,29,1110], 2, 2)
def contains_neighbors_within_2(arr, delta):
    try:
        for x,y,z in arr:
            if abs(x - y) <= delta:
                return True
            elif abs(y - z) <= delta:
                return True
            elif abs(x - z) <= delta:
                return True
    except IndexError: # i.e.
        return False

# Test simple version
print contains_duplicate([1,2,3]) # Return False
print contains_duplicate([1,2,2]) # Returns True

# test for k = 1 and values are next to each other
print contains_duplicate_within_k([1,2,3,3,4], 1) # Return True

# test for k < 1 and values are next to each other
print contains_duplicate_within_k([1,2,3,3,4], 2) # Return True

# test for k = 1 and values are not next to each other
print contains_duplicate_within_k([1,2,3,4,3], 1) # 4-2 <= 1, Return False

# test for k < 1 and values are not next to each other
print contains_duplicate_within_k([1,2,3,4,3], 2) # Return depending on <= k, in this case True

# test no duplicates
print contains_duplicate_within_k([1,2,3,4,5], 3) # Returns False
