from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.window_sum = 0.0
        self.vals = deque([])
        self.size = size

    def next(self, val: int) -> float:
        self.window_sum += val
        self.vals.append(val)
        if len(self.vals) > self.size:
            self.window_sum -= self.vals.popleft()
        return self.window_sum / len(self.vals)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
