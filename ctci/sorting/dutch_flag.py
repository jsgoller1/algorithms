import random
import copy
import sorting

def dutch_flag(array, pivot_index, info=True):
    if(info):
        print("Dutch flag sort")
        print("Time complexity: O(len(array))")
        print("Space complexity: O(c)")
        print("The solution to this problem uses some tricky array index-fu,")
        print("so you will see each step as it occurs (and press any key to")
        print("go to the next step).")
        print("")

    pivot = array[pivot_index]
    #print "Pivot: " + str(pivot)
    smaller = 0
    equal = 0
    larger = len(array)-1
    iterations = 0

    while (equal <= larger): # parsing through every element in the array
        print "Iteration " + str(iterations)
        print "array: " + str(array)
        print "pivot value: " + str(pivot)
        print "smaller: " + str(smaller) + " (%d)" % array[smaller]
        print "equal: " + str(equal) + " (%d)" % array[equal]
        print "larger: " + str(larger) + " (%d)" % array[larger]
        if array[equal] < pivot:
            print "array[equal] < pivot"
            print "Swap array[smaller] with array[equal], then equal++ and smaller++"
            array = swap(array, smaller, equal)
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            print "array[equal] == pivot"
            print "No swapping, equal++"
            equal += 1
        else: # array[equal] > pivot
            print "array[equal] > pivot"
            print "Swap array[equal] and array[larger], larger--"
            array = swap(array, equal, larger)
            larger -= 1
        print "array: " + str(array)
        raw_input("")
        iterations +=1
    return array

def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp
    return array

if __name__ == '__main__':
    my_list = sorting.generate_list(20)
    unsorted = copy.deepcopy(my_list)
    pivot_index = random.randint(0, len(my_list)-1)
    #print("Unsorted: " + str(unsorted))
    sorted_list = dutch_flag(my_list, pivot_index, True)
    print("Sorted: " + str(sorted_list) + "\n")
