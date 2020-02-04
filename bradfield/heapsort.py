def heapsort(arr):
    """
    1) Turn input array into a heap
    2) Divide elements into a sorted and unsorted portion while maintaining
       invariant (which is the heap invariant for the unsorted portion)
    """
    pass


def heapify(arr):
    pass


def sift_down(heap):
    pass


class SortingTestCase:
    def __init__(self, name, actual):
        self.name = name
        self.actual = actual

    def test(self):
        expected = self.actual.copy()
        heapsort(self.actual)
        assert self.actual == sorted(expected)


if __name__ == "__main__":
    test_cases = [
        SortingTestCase("Empty", []),
        SortingTestCase("Singleton", [1]),
        SortingTestCase("Average", [random.randint(-100, 100) for i in range(1000)]),
        SortingTestCase("Sorted", [i for i in range(1000)]),
        SortingTestCase("Perfectly unsorted", list(reversed([i for i in range(1000)]))),
        SortingTestCase("Huge", [random.randint(-100, 100) for i in range(100000)]),
    ]
    for case in test_cases:
        print("Testing: {0}".format(case.name))
        case.test()
