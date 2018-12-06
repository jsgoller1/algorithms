import collections
import random

prioritized_data = collections.namedtuple('prioritzed_data', ['priority', 'data'])

class priority_queue():
    def __init__(self, initial_data=[]):
        self.pq = []
        for item in initial_data:
            self.insert(item)

    def display(self, depth=0, idx=0):
        print(" "*2*depth + "- {0}: {1}".format(depth, self.pq[idx]))
        left = 2*idx+1 if 2*idx+1 < len(self.pq) else 0
        right = 2*idx+2 if 2*idx+2 < len(self.pq) else 0
        if left and left < len(self.pq):
          self.display(depth+1, left)
        if right and right < len(self.pq):
          self.display(depth+1, right)

    def insert(self, priority, data):
        pd = prioritized_data(priority=priority, data=data)
        self.pq.append(pd)
        self._bubble_up(len(self.pq)-1)

    def extract_min(self):
        minimum = self.pq[0]
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self._bubble_down(0)
        return minimum

    def heapsort(self):
        while self.pq:
            yield self.extract_min()

    def _bubble_up(self, idx):
        if idx > 0:
          parent = idx//2
          if self.pq[idx].priority < self.pq[parent].priority:
            self.pq[idx], self.pq[parent] = self.pq[parent], self.pq[idx]
            self._bubble_up(parent)

    def _bubble_down(self, idx):
        left = 2*idx+1 if 2*idx+1 < len(self.pq) else 0
        right = 2*idx+2 if 2*idx+2 < len(self.pq) else 0
        for child in [left,right]:
          if child and self.pq[idx].priority > self.pq[child].priority:
            self.pq[idx], self.pq[child] = self.pq[child], self.pq[idx]
            self._bubble_down(child)


if __name__ == '__main__':
  pq = priority_queue()
  names = ["joshua", "nick", "cj", "justin", "roberto", "jeff", "josh", "jerry", "steve", "clement", "judah"]
  for name in names:
    pq.insert(random.randint(0,100), name)
  pq.display()
  for item in pq.heapsort():
    print(item)
