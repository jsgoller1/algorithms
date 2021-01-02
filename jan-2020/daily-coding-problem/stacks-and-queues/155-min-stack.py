"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
    - pop, top, and get_min() always called on nonempty stacks

Cases:
    - Stack empty
        - Next val becomes min
    - New min is pushed; need to update
        - Push new min to min_values stack 
    - Old min is popped; need to get new min
        - Pop from min_values stack
    - Duplicate mins are pushed
        - Should push them to min values 
-------------------------------------
What if we used two stacks?
    - main stack and mins stack
    - Each time a new val is pushed to main stack, if 
      it's less than the current min, push onto mins stack
    - getmin gets top of mins stack
    - Should we have to push every value onto mins stack? Is
      there a case where we didn't store an intermediary but
      now the stack is wrong?
      push these:  [0, -1,  4, 2]
      top of mins: [0, -1, -1, -1]
      No - because the min will be the min up to that point, and only
      needs to be updated if that min leaves the stack or a new one is introduced

    - If a duplicate min value arises, we should push it to min values:
        pushing: [-2,-2, -1, -2]
        If we then call pop(), we don't want to remove -2 from min values stack
"""


class MinStack:

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if (not self.min_values) or x <= self.min_values[-1]:
            self.min_values.append(x)

    def pop(self) -> None:
        ret = self.values.pop()
        if ret == self.min_values[-1]:
            self.min_values.pop()
        return ret

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
