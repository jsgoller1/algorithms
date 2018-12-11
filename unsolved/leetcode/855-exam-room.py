"""
- In: writing a class that supports seating students as far from other students
as possible, or 0 if no one is sitting there.
- Out: called a bunch of times with set/unset

- Might be able to use binary
  - jk, 10^9 students
  - also probably cannot use direct instantiation of array
- up to 10,000 calls of seat() and leave()
- leave() never called on empty classroom

- This is probably a DS question; what can efficiently tell us
the furthest away we can sit from another student?

-

1 sits at 0(n-1)/1 = 0
2 sits at 1(n-1)/1 = n-1
3 sits at 1(n-1)/2
4 sits at 1(n-1)/4



"""


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """

    def seat(self):
        """
        :rtype: int
        """

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
