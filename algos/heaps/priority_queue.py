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

    def kth_smallest_greater_than(self, k, string, curr=0):
      """
      See Algorithm Design Manual 2nd ed, 4.3.4 (p. 116). Note the difference
      here from the stated function in the textbook due to implementation;
      because we are storing strings and determining the priority of a string
      independently from the string itself, we are asking if the
      kth highest priority string is lexicographically greater than :string (i.e.
      it would come after :string in an English dictionary). This still has the
      same runtime as the given implementation in the textbook, O(k).
      """
      print("curr: {0}".format(curr))
      if curr >= len(self.pq):
        return False
      if curr == k-1:
        print("{0}th smallest: {1}".format(k, self.pq[curr]))
        return self.pq[curr].data > string
      if curr < k-1:
        return self.kth_smallest_greater_than(k, string, 2*curr+1) or self.kth_smallest_greater_than(k, string, 2*curr+2)

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
  print(pq.kth_smallest_greater_than(7, "david"))
  for item in pq.heapsort():
    print(item)
