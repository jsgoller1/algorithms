from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self._data = deque([])
        self._size = size
        self._rsum = 0

    def next(self, val: int) -> float:
        self._data.append(val)
        self._rsum += val
        if len(self._data) > self._size:
            out = self._data.popleft()
            self._rsum -= out
        return self._rsum / len(self._data)


for data, results in [
    ([1, 10, 3, 5], [1.0, 5.5, 4.66667, 6.0]),
    ([10, 10, 10, 5], [10.0, 10.0, 10.0, 8.334])

]:
    ma = MovingAverage(3)
    for action, result in zip(data, results):
        actual = ma.next(action)
        expected = result
        assert abs(actual - expected) < .001, f"{actual} != {expected}"
