"""
I got this variant of this question as a TPS for a FAANG company in 2023. 

Design and implement an iterator for an embedded list like : {1,{2, 3}, 4, 5}. 
The element in the list can be either an int or a list of int. The iterator is expected to iterate over it, and generate an iterables of ints as 1,2,3,4,5

[1, 3, [4], [[4, [5]]]] -> [1,3,4,4,5] (printed one at a time)
[[[[[[[[[[[[[[[],[5]]]]]]]]]]]]]]]
- next(), hasNext()

[[], [1]]
    (0, [])
        

Constraints:
- input list fits in memory
- -INT_MAX <= input_list[i] <= INT_MAX
- no recursive call depth limit (default: 3k)
- lists or ints
- sublists could be empty 

[
    (4, [1, 3, [4], [[4, [5]]]])
    (0, [[4, [5]]]),
    (0, [4, [5]]),
    
]

1
3
4

stack = []
stack.append(arr[0])
"""

def flatten(list_or_int, result):
    for item in nested_list:
        if isinstance(list_or_int, int):
            result.append(list_or_int)
        flatten(list_or_int, result)

class NestedListIteratorLinear:
    def __init__(self, nested_list):
        self._i = 0
        self._data = []
        flatten(nested_list, self._data)
        
    def next(self):
        if not self._has_nest():
            raise StopIteration
        ret = self._data[self._i]
        self._i += 1
        return ret
    
    def has_next(self):
        return self._i < len(self._data)


"""
input = [1, 3, [4], [[4, [5]]]]
self._data = []
flatten([1, 3, [4], [[4, [5]]]], [])
    -> append(1, [])
    -> append(3, [1])
    -> flatten([4], [1,3])
        -> append(4, [1,3])
    -> flatten([[4, [5]]], [1,3,4])
        -> flatten([4, [5]], [1,3,4])
            -> append(4, [1,3,4])
            -> flatten([5], [1,3,4,4])
                -> append(5, [1,3,4,4])
->
[1,3,4,4,5]
""



# TODO: use good type hints
class NestedListIterator:
    def __init__(self, input_list):
        self._stack = [(0, input_list)] if input_list else []
        
    def next(self) -> int:
        if not self._stack:
            raise StopIteration
        i, frame = self._stack.pop()
        curr = frame[i]
        while isinstance(curr, list):
            self._stack.append((i+1, frame)) # NOTE: handle case where i is last element
            if curr:
                self._stack.append((0, curr))
                curr = curr[0]
            else:
                i, curr = self._stack.pop()
        if i+1 < len(frame):
            self._stack.append((i+1, frame))
        return curr
                        
    def has_next(self) -> bool:
        return len(self._stack) > 0
        

"""
input = [1, 3, [4], [[4, [5]]]]
    -> [(0, input[0])]
    -> next() = 1
    -> [(1, input[0])]
    -> next() = 3
    -> [(2, input[0])]
    -> next()
    -> [(2, input[0]), (0, input[2])]
     
""
