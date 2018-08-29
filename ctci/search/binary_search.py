import random
import copy
import pdb

def binarySearch(array, value, info=True):
    array.sort()
    begin = 0
    end = len(array)-1
    if value > array[end] or value < array[begin]: # Eliminate unnecessary searches
        print("O(c) disqualified")
        return False
    while (begin <= end):
        pivot = (begin+end)/2
        if value < array[pivot]: # value is in the lower part
            end = pivot-1
            continue
        elif value > array[pivot]: # value is in the upper part
            begin = pivot+1
            continue
        else: # array[pivot] == value, victory!
            return pivot
    return False

if __name__ == '__main__':
    array = [random.randint(0, 100) for x in range(random.randint(1, 20))]
    if (raw_input("Do you want to search for a value necessarily in the array (y) or one generate one randomly (n)? ") == "y"):
        value = array[random.randint(0, len(array)-1)]
    else:
        value = random.randint(0, 100)
    found = binarySearch(array, value)
    print("array: " + str(array))
    print("value: " + str(value))
    print("index (False if element isn't found): " +str(found))
