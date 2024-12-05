"""
it = iter([1,2,3])
assert it.__next__() == 1
assert it.__next__() == 2
assert it.__next__() == 3
with pytest.raises(StopIteration):
    it.__next__()

it = resumable_iter([1,2,3])
assert it.__next__() == 1
s = it.get_state()
assert it.__next__() == 2
assert it.__next__() == 3
it.set_state(s)  # go back to previous point of iteration!
assert it.__next__() == 2
assert it.__next__() == 3

In your language of choice, write an interface or abstract class for resumable iterators with operations next(), get_state(), set_state(s). You do not need to implement the interface.
Write a test function, e.g. def test_resumable_iterator(it, expected_elements): ... for your new interface exercising the functionality. It should test that iteration works as expected, and that resumption works at every state. The test should pass for any implementation of the interface, with only the assumption that there are only finitely many elements!
-----
Constraints:
    - types within iterable: could be any comparable types, could be heterogenous
    - iterable fits in memory
    - for test, initialize iterator first 
    - basic python iterator 
"""

# TODO: use good type hints
# TODO: use ABC class


class ResumableIterator:
    def __init__(self, iterable):
        pass

    # NOTE: skipping __iter__()

    def __next__(self):
        pass

    def get_state(self):
        pass

    def set_state(self, i: int):
        pass


def test_resumable_iterator(it: ResumableIterator, expected_elements):
    # TODO: at least two element
    states = []

    # Basic happy path
    for i, expected in enumerate(expected_elements):
        states.append(it.get_state())
        actual = next(it)
        assert actual == expected, f"item {i} mismatch: {actual} != {expected}"

    # Confirm state get/save works
    for i, state in enumerate(states):
        it.set_state(state)
        if i == len(states):
            try:
                next(it)
            except StopIteration:
                pass
            else:
                raise AssertionError("Didn't raise StopIteration on last state")
        else:
            expected = expected_elements[i]
            actual = next(it)
            assert actual == expected

    # Try calling next() repeatedly
    for i, state in enumerate(states):
        it.set_state(states[i])
        next_called = 0
        expected_calls = len(states)-i
        while next_called < expected_calls:
            try:
                next(it)
                next_called += 1
            except StopIteration:
                break
        assert next_called == expected_calls, f"Incorrect number of next(): {next_called} != {expected_calls}"


class ListIterator(ResumableIterator):
    def __init__(self, lst):
        self.data = lst
        self.idx = 0
        self.limit = len(lst)

    def __next__(self):
        if self.idx >= self.limit:
            raise StopIteration

        val = self.data[self.idx]
        self.idx += 1
        return val

    def get_state(self):
        return self.idx

    def set_state(self, i: int):
        # TODO: Check for negative
        self.idx = i


lst = [1, 2, 3, 4, 5]
it = ListIterator(lst)
test_resumable_iterator(it, lst)

"""
class JsonlFileIterator(ResumableIterator):
    def __init__(self, filename):

d0.jsonl:
    {"item": 1}
    {"item": 2}
d1.jsonl:
    {"item": 3}
    {"item": 4}
    {"item": 5}
d2.jsonl:
    {"item": 6}
    {"item": 7}
d3.jsonl: <empty>
d4.jsonl:
    {"item": 8}
"""


def JsonlFileIterator(filename):
    return ListIterator({
        "d0.jsonl": [1, 2],
        "d1.jsonl": [3, 4, 5],
        "d2.jsonl": [6, 7],
        "d3.jsonl": [],
        "d4.jsonl": [8],
    }[filename])


filenames = [f"d{i}.jsonl" for i in range(5)]
expected_elements = [1, 2, 3, 4, 5, 6, 7, 8]


class MultiFileIterator(ResumableIterator):
    def __init__(self, file_list):
        self.file_list = file_list
        self.it_idx = 0
        self.it = JsonlFileIterator(file_list[0])

    def __next__(self):
        while True:
            try:
                return next(it)
            except StopIteration:
                if self.it_idx == len(self.file_list)-1:
                    raise
                else:
                    self.it_idx += 1
                    self.it = JsonlFileIterator(self.file_list[self.it_idx])

    def get_state(self):
        return (self.it_idx, self.it.get_state())

    def set_state(self, file_idx, line_idx):
        if not (0 <= file_idx <= len(self.file_list)):
            return None

        self.it = JsonlFileIterator(self.file_list[file_idx])
        self.it_idx = file_idx
        self.it.set_state(line_idx)
