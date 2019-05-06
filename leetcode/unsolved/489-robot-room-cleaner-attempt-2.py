"""
Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made
is 90 degrees. When it tries to move into a blocked cell, its bumper sensor detects the obstacle
and it stays on the current cell. Design an algorithm to clean the entire room using only the 4
given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Notes:
- The input is only given to initialize the room and the robot's position internally.
  You must solve this problem "blindfolded". In other words, you must control the robot
  using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
- The robot's initial position will always be in an accessible cell.
- The initial direction of the robot will be facing up.
- All accessible cells are connected, which means the all cells marked as 1 will be
  accessible by the robot.
- Assume all four edges of the grid are all surrounded by wall.
---------------------------------------------------------------
- In: Grid, starting position
- Out: set of behaviors such that all cells are visited
- Cases:
  - Fully explorable room
  - Completely unexplorable room
  - Variants

- clean() is a red herring. We just need to visit every cell.
- A BFS or DFS will ensure we visit every cell; however, for a BFS,
we can wind up in an invalid state - we cannot explore a cell we are not
next to currently, so if we try to visit the neighbor of a cell we were
in previously, we could have trouble. DFS is probably a better option.
- We do not actually know what cell we are in when we start; however
we can just assume we're in 0,0 and go from there; we won't worry about
array index errors since move() will return false.
- We don't have access to the grid, just the robot; as such, we need to
program our DFS from turning and moving
- Perhaps we should implement Solution methods that match
the robot's methods and in each call update the internal representation
as well as call the robot API?
- Our overall algorithm should be something like:
  visit(cell, parent):
    clean()
    for each neighbor:
      face(neighbor) # turns robot correctly
      if move(): # moves robot forward
        visit_current_cell(neighbor, current)
    face(parent)
    move() # final move will return false, which is OK.
- The best thing to do would be if we could completely abstract away direction
from our high level algorithm; maybe if we implement a moveTo() that handles
correctly facing?
- Our overall algorithm should be something like:
  visit(cell, parent):
    clean()
    for each neighbor:
      if moveTo(): # moves robot forward
        visit_current_cell(neighbor, current)
    moveTo(parent) # final move will return false, which is OK.

  moveTo(src, dst):
    # turn to face correct direction;
    # if move() succeeds, update position and return true
    # if move() fails, don't update position and return false

  face(src, dest):
    # determine which direction in the list should be faced
    # call robot.turnLeft() or turnRight() until facing that direction
"""

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, 1)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


class Solution(object):
    def __init__(self):
        self.visited = set()
        self.position = (0, 0)  # assumed
        self.directions_i = 0

    def cleanRoom(self, robot):
        self.robot = robot
        self.visit(robot, self.position)  # what should the parent of the first cell be?

    def visit(self, cell, parent):
        """
        clean()
        for each neighbor:
          if moveTo(): # moves robot forward
            visit_current_cell(neighbor, current)
        moveTo(parent) # final move will return false, which is OK.
        """
        self.visited.add((self.row, self.col))
        self.robot.clean()
        return

    # returns true if next cell is open and robot moves into the cell.
    # returns false if next cell is obstacle and robot stays on the current cell.
    def moveTo(self, cell):
        self.face(cell)
        if self.robot.move():
            self.position[0] += DIRECTIONS[self.directions_i][0]
            self.position[1] += DIRECTIONS[self.directions_i][1]
            return True
        return False

    # Ensure the robot is facing in the correct direction to move to
    # this cell; turn right until so.
    def face(self, cell):
        correct_direction = (cell[0] - self.position[0], cell[1] - self.position[1])
        if correct_direction not in DIRECTIONS:  # diagonal or other invalid direction
            return
        while DIRECTIONS[self.directions_i] != correct_direction:
            self.robot.turnRight()
            self.directions_i = (self.directions_i + 1) % 4


if __name__ == '__main__':
    s = Solution()
