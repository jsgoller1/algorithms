import random
import copy
import sorting

def bubblesort(array, info=True):
    if(info):
        print("Bubble sort")
        print("Time complexity: O(n^2)")
        print("Space complexity: O(c)")
    try:
        assert(isinstance(array, list))
        assert(array != [])
    except AssertionError:
        return False

    for each in range(len(array)):
        for other in range(len(array)-1):
            if array[other+1] < array[other]:
                temp = array[other]
                array[other] = array[other+1]
                array[other+1] = temp
    return array

if __name__ == '__main__':
    my_list = sorting.generate_list(20)
    unsorted = copy.deepcopy(my_list)
    sorted_list = bubblesort(my_list, True)
    print("Unsorted: " + str(unsorted))
    print("Sorted: " + str(sorted_list) + "\n")
