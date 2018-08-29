import random
import copy
import pdb

def linear_search(array, value, info=True):
    for each in array:
        if value == each:
            return array.index(each)
    return False

if __name__ == '__main__':
    array = [random.randint(0, 100) for x in range(random.randint(1, 20))]
    value = array[random.randint(0, len(array)-1)]
    found = linear_search(array, value)
    print("array: " + str(array))
    print("value: " + str(value))
    print("index: " +str(found))
