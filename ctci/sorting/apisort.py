import random
import copy
import sorting

def api_sort(array, info=True):
    if(info):
        print("API sort")
        print("This function just uses the list's .sort() method, which is actually timsort.")
        print("In an actual software dev situation, don't reinvent the wheel; use the API!")
    try:
        assert(isinstance(array, list))
    except AssertionError:
        return False
    array.sort()
    return array

if __name__ == '__main__':
    myList = sorting.generate_list(20)
    unsorted = copy.deepcopy(myList)
    sortedList = api_sort(myList, True)
    print("Unsorted: " + str(unsorted))
    print("Sorted: " + str(sortedList) + "\n")
