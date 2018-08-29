import random
import copy
import sorting

def mergesort(array, info=True):
    if(info):
        print("Merge sort")
        print("Time complexity: O(n*log(n))")
        print("Space complexity: O(n)")
    try:
        assert(isinstance(array, list))
    except AssertionError:
        return False

    if len(array) <= 1:
        return array #empty and singleton lists are sorted by definition
    middle = len(array)/2
    left = array[0:middle]
    right = array[middle:len(array)]
    left = mergesort(left, False)
    right = mergesort(right, False)
    sorted_array = merge(left,right)
    return sorted_array

def merge(left,right):
    sorted_array = []
    while(right != [] or left != []):
        try:
            which = left[0] <= right[0]
            if which:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
        except IndexError: #one of the lists is empty
            if(right == left == []):
                return sorted_array
            if left == []:
                sorted_array.append(right.pop(0))
            elif right == []:
                sorted_array.append(left.pop(0))
    return sorted_array

if __name__ == '__main__':
    my_list = sorting.generate_list(20)
    unsorted = copy.deepcopy(my_list)
    sorted_list = mergesort(my_list, True)
    print("Unsorted: " + str(unsorted))
    print("Sorted: " + str(sorted_list) + "\n")
