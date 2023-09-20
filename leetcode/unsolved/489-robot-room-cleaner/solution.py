# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


"""
Summary: DFS with dictionary for a kind of primitive SLAM. 

enum directions = {up, down, left, right}
directions_to_deltas: {
    up: (-1, 0), 
    down: (1, 0), 
    left: (0, 1), 
    right: (0, -1)
}

higher level robot API and state:
- robot.position = (0,0)
- robot.orientation = up
- robot.move_direction(direction): moves the robot one cell in the given direction from its current
  cell. It handles turning appropriately, but makes not guarantees about orientation once complete. Returns
  the bool from the lower level move function

pseudo(robot):
    robot.clean() # cleans (0,0)
    visited = {(0,0)}

    # the DFS will explore the entire grid by making all possible "moves"
    # from every cell. Every "move" we have yet to make goes into the stack, and 
    # each time we make a successful move, we have to push its inverse to the
    # grid to undo it and get back to the previous place. 
    stack = [
        (up),
        (down),
        (left),
        (right)
    ] 
    while stack nonempty:
        move popped from stack
        if current cell + move has already been visited:
            skip everything, pop next move.
        try the move
        if it succeeds:
            - first push the inverse (left for right, up for down, etc) to the stack. The robot doesn't need
            to know if a move is an inverse or not; if we move left, push "right" onto the stack
            - calculate the current cell location by adding the successful move to the last known location
            clean the current cell
            - add the current cell to visited
            - then for each possible move from this cell:
                - new possible cell is current cell + move
                - if new possible cell isn't in visited yet, push the move to the stack
        otherwise:
            - move failed, so add the cell that would've been reached to visited
    return 

"""
